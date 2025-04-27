from MyBot.world.grid import Grid
from MyBot.movement.move import Position
from MyBot.config import MAX_ENERGY, DIRECTIONS, RECHARGE_COST, GRID_WIDTH, GRID_HEIGHT
import random



"""
Bot Manager module for MyBot system.

Handles bot creation, movement, energy management, 
recharging, random movement, and shutdown operations.
"""




class Bot:
    """
    A single bot that can move and remember what it's done.
    """

    def __init__(self, bot_id, grid):
        # Each bot has a name (or ID) and starts at position (0,0)
        self.bot_id = bot_id
        self.position = Position()
        self.log = []  # Keep track of movements (like a mini history)
        
        #adding energy levels --more features
        self.energy = MAX_ENERGY  # Bots start with 10 moves worth of energy
        self.balance = 10  # Start each bot with 10 coins
        self.grid = grid  # Save grid reference
        
        
        # Assign a random goal when bot is created
        self.goal = self._generate_random_goal()
        
        
    def _generate_random_goal(self):
        """
        Pick a random location on the grid as the bot's goal.
        """
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        return (x, y)



    #complete revamp for multiplayer
    def move(self, direction):
        
        """
        Try to move in the given direction.
        Predict the move first: check for energy, collisions with other bots, and grid boundaries.
        Only execute move if it is safe.
        """

        #Step 1: Check if bot has enough energy
        if self.energy <= 0:
            self.log.append("[ERROR] Not enough energy to move.")
            raise ValueError("Bot is out of energy and cannot move.")

        #Step 2: Save the current position (in case we need to rollback or predict)
        old_x, old_y = self.position.x, self.position.y

        #Step 3: Predict the next position without actually moving yet
        if direction == "up":
            new_x, new_y = old_x, old_y + 1
        elif direction == "down":
            new_x, new_y = old_x, old_y - 1
        elif direction == "left":
            new_x, new_y = old_x - 1, old_y
        elif direction == "right":
            new_x, new_y = old_x + 1, old_y
        elif direction == "up-right":
            new_x, new_y = old_x + 1, old_y + 1
        elif direction == "up-left":
            new_x, new_y = old_x - 1, old_y + 1
        elif direction == "down-right":
            new_x, new_y = old_x + 1, old_y - 1
        elif direction == "down-left":
            new_x, new_y = old_x - 1, old_y - 1
        else:
            self.log.append("[ERROR] Invalid direction.")
            raise ValueError(f"Invalid direction: {direction}")

        #Step 4: Check if the new position is already occupied by another bot
        if self.grid.manager.is_position_occupied(new_x, new_y):
            self.log.append(f"[ERROR] Move blocked: another bot is at ({new_x}, {new_y}).")
            raise ValueError("Cannot move: another bot is already at that location.")

        #Step 5: Actually perform the move using the Position class
        try:
            # move.py will handle out-of-bounds rollback automatically if needed
            self.position.move(direction)

            #Step 6: Update energy cost (diagonal moves cost 2, straight moves cost 1)
            if "-" in direction:
                self.energy -= 2
            else:
                self.energy -= 1

            coords = self.position.get_coords()

            #Step 7: Recharge if landing on a charging station
            if self.grid.is_charging_station(coords[0], coords[1]):
                self.energy = MAX_ENERGY
                self.log.append(f"[RECHARGED] Recharged automatically at station {coords}.")

            #Step 8: Check if goal is reached
            if coords == self.goal:
                self.log.append(f"[GOAL] Reached target at {self.goal}!")
                
            
            #Step 8.5: Check if bot captures the shared goal
            if (
                self.grid.manager.shared_goal and
                not self.grid.manager.shared_goal_claimed and
                coords == self.grid.manager.shared_goal
            ):
                self.grid.manager.shared_goal_claimed = True
                self.balance += 5  # Bonus for capturing shared goal
                self.log.append(f"[COMPETITION] Captured the shared goal at {coords}! +5 coins awarded.")


            #Step 9: Log the successful move
            self.log.append(f"Moved {direction} to {coords}. Energy left: {self.energy}")
            return coords

        except ValueError as e:
            #If move.py raised a ValueError (out of bounds, etc), log it too
            self.log.append(f"[ERROR] {str(e)}")
            raise





    def status(self):
        """
        Return current position and last few actions.
        """
        return {
            "bot_id": self.bot_id,
            "position": self.position.get_coords(),
            "log": self.log[-5:]  # Only show the last 5 things
        }
        
        
    def recharge(self):
        """
        Refill the bot's energy back to maximum.
        """
        self.energy = MAX_ENERGY
                
        self.balance -= RECHARGE_COST

        self.log.append("Recharged to full energy.")
        
        
    def reset(self):
        """
        Reset the bot's position to (0,0), full energy, and clear the log.
        """
        self.position = Position()
        self.energy = MAX_ENERGY
        self.log = []

        
        
    



class BotManager:
    """
    Keeps track of all bots that are created.
    Handles create, move, and status requests.
    """

    def __init__(self):
        # Store all bots in a dictionary with their ID as the key
        self.bots = {}
        self.grid = Grid()  # grid object!
        self.shared_goal = None  # Track the competitive goal (x, y)
        self.shared_goal_claimed = False  # Track if goal is captured


        


    def create_bot(self, bot_id):
        """
        Make a new bot with a unique ID.
        If the ID already exists, show an error.
        """
        
        if bot_id in self.bots:
            raise ValueError(f"Bot '{bot_id}' already exists.")
        self.bots[bot_id] = Bot(bot_id, self.grid)  # pass grid to bots!
        return f"Bot '{bot_id}' created."


    def move_bot(self, bot_id, direction):
        """
        Move the selected bot in the given direction.
        """
        return self._get_bot(bot_id).move(direction)


    def get_status(self, bot_id):
        """
        Return position + log for the selected bot.
        """
        return self._get_bot(bot_id).status()
    
    
    def shutdown_bot(self, bot_id):
        """
        Remove a bot from the manager.

        Deletes the bot instance if it exists.
        Raises an error if the bot ID is not found.
        """
        if bot_id not in self.bots:
            raise ValueError(f"Bot '{bot_id}' not found.")
        del self.bots[bot_id]
        return f"Bot '{bot_id}' has been shut down."
    
    
    def list_bots(self):
        """
        Return a list of all active bot IDs.
        """
        return list(self.bots.keys())



    def _get_bot(self, bot_id):
        """
        Helper method to find a bot or raise error if not found.
        """
        if bot_id not in self.bots:
            raise ValueError(f"Bot '{bot_id}' not found.")
        return self.bots[bot_id]
    
    
    
    def is_position_occupied(self, x, y):
        """
        Check if any bot is currently at (x, y).
        """
        for bot in self.bots.values():
            if bot.position.x == x and bot.position.y == y:
                return True
        return False
    
    

    def recharge_bot(self, bot_id):
        """
        Recharges a bot's energy to full.

        Raises an error if the bot does not exist.
        """
        return self._get_bot(bot_id).recharge()
    
    
    
    def get_energy(self, bot_id):
        """
        Return the current energy of the bot.

        Raises an error if the bot is not found.
        """
        return self._get_bot(bot_id).energy
    
    
    
    def move_random(self, bot_id):
        """
        Move the bot in a random valid direction.
        """
        direction = random.choice(DIRECTIONS)
        return self.move_bot(bot_id, direction)
    
    



    
    
