"""
Configuration file for MyBot System.

Contains constants for grid size, bot settings, energy management, 
and movement options. Centralized here for easy maintenance and scaling.
"""



# Constants for grid size
GRID_WIDTH = 10
GRID_HEIGHT = 10

# Default starting energy for new bots
MAX_ENERGY = 10

# Possible directions for bot movement
DIRECTIONS = ["up", "down", "left", "right", "up-right", "up-left", "down-right", "down-left"]

# Cost (in virtual currency) to fully recharge a bot
RECHARGE_COST = 5


# App metadata
__version__ = "1.0.0"
