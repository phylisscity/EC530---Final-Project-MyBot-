# Import necessary modules from Flask
from flask import Blueprint, request, jsonify
from MyBot.bot_manager import BotManager



# Create a Blueprint to organize the API routes separately from the main app
# This allows the app to stay modular and scalable
bp = Blueprint("api", __name__)



# Instantiate a single BotManager to handle all bot-related actions
# All API routes will use this manager to control bots
manager = BotManager()



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
        # If bot is out of energy or not found, handle it nicely
        return jsonify({"error": str(e)}), 400



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
    
    
@bp.route("/list", methods=["GET"])
def list_bots():
    """
    Return a list of all active bot IDs.

    Useful for checking which bots are currently active in the system.
    """
    return jsonify({"bots": manager.list_bots()})



