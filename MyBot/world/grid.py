import random
from MyBot.config import GRID_WIDTH, GRID_HEIGHT



def is_within_bounds(x, y, width, height):
    """
    Check if (x, y) is inside a grid of given width and height.
    """
    return 0 <= x < width and 0 <= y < height

class Grid:
    """
    Represents the virtual world grid and special locations (like charging stations).
    """

    def __init__(self, num_stations=5):
        self.width = GRID_WIDTH
        self.height = GRID_HEIGHT
        self.charging_stations = self._generate_charging_stations(num_stations)


    def _generate_charging_stations(self, count):
        """
        Randomly place a set number of charging stations on the grid.
        """
        stations = set()
        while len(stations) < count:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            stations.add((x, y))
        return list(stations)


    def is_charging_station(self, x, y):
        """
        Check if the given (x,y) is a charging station.
        """
        return (x, y) in self.charging_stations
