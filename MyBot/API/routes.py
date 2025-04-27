# Import necessary modules from Flask
from flask import Blueprint, request, jsonify
from MyBot.bot_manager import BotManager

from MyBot.config import DIRECTIONS
from MyBot.config import RECHARGE_COST
from MyBot.config import GRID_WIDTH, GRID_HEIGHT
import random



# Create a Blueprint to organize the API routes separately from the main app
# This allows the app to stay modular and scalable
bp = Blueprint("api", __name__)



# Instantiate a single BotManager to handle all bot-related actions
# All API routes will use this manager to control bots
manager = BotManager()


#create bot
@bp.route("/create", methods=["POST"])
def create_bot():
    
    """
    API endpoint to create a new bot.

    Expects JSON input: { "bot_id": "desired_bot_name" }
    
    Returns:
    - Success: { "message": "Bot 'xyz' created." }
    - Failure: { "error": "Bot already exists" } or { "error": "Missing bot_id" }
    """
    
    data = request.json
    bot_id = data.get("bot_id")  # Extract bot ID from incoming request

    # Check if the client sent a bot_id
    if not bot_id:
        return jsonify({"error": "Missing bot_id"}), 400

    try:
        # Create the bot and return a success message
        message = manager.create_bot(bot_id)
        return jsonify({"message": message})
    except ValueError as e:
        # Handle case where bot_id already exists
        return jsonify({"error": str(e)}), 400




#move bot
@bp.route("/move/<bot_id>", methods=["POST"])
def move_bot(bot_id):
    """
    API endpoint to move an existing bot in a specific direction.

    URL Parameter:
    - bot_id: ID of the bot to move

    Expects JSON input: { "direction": "up" } (or down, left, right)

    Returns:
    - Updated bot status (position and log)
    - Or an error if the bot_id doesn't exist or the direction is invalid
    """
    
    data = request.json
    direction = data.get("direction")  # Get direction from incoming request

    # Check if the client provided a direction
    if not direction:
        return jsonify({"error": "Missing direction"}), 400

    try:
        # Move the bot and return updated status
        manager.move_bot(bot_id, direction)
        
        return jsonify(manager.get_status(bot_id))
    
    except ValueError as e:
        # Handle cases like invalid direction, out of bounds, or no energy left
        return jsonify({"error": str(e)}), 400




#get bot status
@bp.route("/status/<bot_id>", methods=["GET"])
def bot_status(bot_id):
    """
    API endpoint to get the current status of a bot.

    URL Parameter:
    - bot_id: ID of the bot to retrieve

    Returns:
    - The bot's current position and recent movement log
    - Or an error if the bot_id does not exist
    """
    try:
        # Retrieve and return the bot's latest status
        return jsonify(manager.get_status(bot_id))
    except ValueError as e:
        # Handle case where bot_id is not found
        return jsonify({"error": str(e)}), 404
    
    
    

#shutdown bot
@bp.route("/shutdown/<bot_id>", methods=["DELETE"])
def shutdown_bot(bot_id):
    
    """
    Remove a bot from the system.

    Deletes the specified bot and returns a confirmation message.
    If the bot does not exist, returns an error.
    """
    try:
        message = manager.shutdown_bot(bot_id)
        return jsonify({"message": message})
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    
    
    
#list bots
@bp.route("/list", methods=["GET"])
def list_bots():
    """
    Return a list of all active bot IDs.

    Useful for checking which bots are currently active in the system.
    """
    return jsonify({"bots": manager.list_bots()})



#recharge bots
@bp.route("/recharge/<bot_id>", methods=["POST"])
def recharge_bot(bot_id):
    """
    Recharge a bot's energy back to full.

    URL Parameter:
    - bot_id: ID of the bot to recharge

    Returns:
    - Success message or an error if the bot does not exist
    """
    try:
        manager.recharge_bot(bot_id)
        return jsonify({"message": f"Bot '{bot_id}' has been recharged to full energy."})
    except ValueError as e:
        return jsonify({"error": str(e)}), 404



#check energy
@bp.route("/energy/<bot_id>", methods=["GET"])
def check_energy(bot_id):
    """
    API endpoint to get the current energy of a bot.

    URL Parameter:
    - bot_id: ID of the bot to check

    Returns:
    - Current energy level
    - Or error if bot doesn't exist
    """
    try:
        energy = manager.get_energy(bot_id)
        return jsonify({"bot_id": bot_id, "energy": energy})
    except ValueError as e:
        return jsonify({"error": str(e)}), 404



#help menu
@bp.route("/help", methods=["GET"])
def help_menu():
    """
    API endpoint to list all available bot actions and their descriptions.
    """
    actions = {
        "/create (POST)": "Create a new bot. Requires { 'bot_id': 'your_bot_id' } in body.",
        "/move/<bot_id> (POST)": "Move the bot in a direction (up/down/left/right). Body: { 'direction': '...' }",
        "/status/<bot_id> (GET)": "Get the bot's current position, recent moves, and energy status.",
        "/energy/<bot_id> (GET)": "Get the bot's current energy level.",
        "/recharge/<bot_id> (POST)": "Recharge the bot's energy back to full (costs coins).",
        "/shutdown/<bot_id> (DELETE)": "Shutdown (delete) a bot.",
        "/list (GET)": "List all active bots."
    }
    return jsonify(actions)



#balance
@bp.route("/balance/<bot_id>", methods=["GET"])
def get_balance(bot_id):
    """
    API endpoint to retrieve the current coin balance of a bot.

    URL Parameter:
    - bot_id: ID of the bot to check

    Returns:
    - JSON with bot_id and balance
    - Or an error if the bot_id is invalid
    """
    try:
        bot = manager._get_bot(bot_id)
        return jsonify({
            "bot_id": bot.bot_id,
            "balance": bot.balance
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 404



#reset bot
@bp.route("/reset/<bot_id>", methods=["POST"])
def reset_bot(bot_id):
    """
    API endpoint to reset a bot to initial position, full energy, and empty log.

    URL Parameter:
    - bot_id: ID of the bot to reset

    Returns:
    - JSON message confirming reset
    """
    try:
        bot = manager._get_bot(bot_id)
        bot.reset()
        return jsonify({"message": f"Bot '{bot_id}' has been reset."})
    except ValueError as e:
        return jsonify({"error": str(e)}), 404



#move random
@bp.route("/move_random/<bot_id>", methods=["POST"])
def move_random(bot_id):
    """
    API endpoint to move a bot randomly in one direction.
    """
    try:
        manager.move_random(bot_id)
        return jsonify(manager.get_status(bot_id))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400



# View current goal
@bp.route("/goal/<bot_id>", methods=["GET"])
def get_goal(bot_id):
    """
    API endpoint to get the current goal location of a bot.

    URL Parameter:
    - bot_id: ID of the bot to check

    Returns:
    - The bot's goal position
    """
    try:
        bot = manager._get_bot(bot_id)
        return jsonify({
            "bot_id": bot.bot_id,
            "goal": bot.goal
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 404




#create shared goal
@bp.route("/create_shared_goal", methods=["POST"])
def create_shared_goal():
    """
    Set a new shared competitive goal for all bots to race toward.
    """
    manager.shared_goal = (
        random.randint(0, GRID_WIDTH - 1),
        random.randint(0, GRID_HEIGHT - 1)
    )
    manager.shared_goal_claimed = False
    return jsonify({"shared_goal": manager.shared_goal})



#get/view shared goal
@bp.route("/shared_goal", methods=["GET"])
def get_shared_goal():
    """
    Get the current shared competitive goal.
    """
    if manager.shared_goal and not manager.shared_goal_claimed:
        return jsonify({"shared_goal": manager.shared_goal})
    else:
        return jsonify({"message": "No active shared goal."})


#messaging
@bp.route("/send_message/<sender_id>/<receiver_id>", methods=["POST"])
def send_message(sender_id, receiver_id):
    """
    API endpoint for a bot to send a message to another bot.
    """
    try:
        data = request.get_json()
        message = data.get("message")

        if not message:
            return jsonify({"error": "Missing 'message' in request body."}), 400

        manager.send_message(sender_id, receiver_id, message)
        
        return jsonify({
            "message": "Message sent successfully.",
            "from": sender_id,
            "to": receiver_id,
            "content": message
        })

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
