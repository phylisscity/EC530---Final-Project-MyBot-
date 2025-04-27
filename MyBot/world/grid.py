# Grid-related logic (placeholder for now)
from MyBot.config import GRID_WIDTH, GRID_HEIGHT


def is_within_bounds(x, y, width, height):
    """
    Check if (x, y) is inside a grid of given width and height.
    """
    return 0 <= x < width and 0 <= y < height
