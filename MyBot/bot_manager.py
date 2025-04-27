from MyBot.movement.move import Position

import random


#random directions
DIRECTIONS = ["up", "down", "left", "right"]


# Default starting energy for new bots
MAX_ENERGY = 10


# Cost (in virtual currency) to fully recharge
RECHARGE_COST = 5


class Bot:
    """
    A single bot that can move and remember what it's done.
    """

    def __init__(self, bot_id):
        # Each bot has a name (or ID) and starts at position (0,0)
        self.bot_id = bot_id
        self.position = Position()
        self.log = []  # Keep track of movements (like a mini history)
        #adding energy levels --more features
        self.energy = MAX_ENERGY  # Bots start with 10 moves worth of energy
        self.balance = 10  # Start each bot with 10 coins


    def move(self, direction):
        """
        Try to move in the given direction (up/down/left/right).
        If direction is invalid, log the error.
        """
        #incorporating energy feature
        
        if self.energy <= 0:
            self.log.append("[ERROR] Not enough energy to move.")
            raise ValueError("Bot is out of energy and cannot move.")

        try:
            self.position.move(direction)
            self.energy -= 1  # Reduce energy by 1 move
            coords = self.position.get_coords()
            self.log.append(f"Moved {direction} to {coords}. Energy left: {self.energy}")
            return coords
        except ValueError as e:
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
        


    def create_bot(self, bot_id):
        """
        Make a new bot with a unique ID.
        If the ID already exists, show an error.
        """
        if bot_id in self.bots:
            raise ValueError(f"Bot '{bot_id}' already exists.")
        self.bots[bot_id] = Bot(bot_id)
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



    
    
