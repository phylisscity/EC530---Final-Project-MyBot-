
#grid
# Constants defining the size of the grid
GRID_WIDTH = 10
GRID_HEIGHT = 10



class Position:
    """Tracks and updates the x, y position of a bot on a grid."""



    def __init__(self, x=0, y=0):
        # Start at given coordinates (default to 0,0)
        self.x = x
        self.y = y



    def move(self, direction):
        """Update the position based on direction input."""
        if direction == "up":
            self.y += 1
        elif direction == "down":
            self.y -= 1
        elif direction == "left":
            self.x -= 1
        elif direction == "right":
            self.x += 1
        else:
            raise ValueError(f"Invalid direction: {direction}")



    def get_coords(self):
        """Return the current (x, y) position as a tuple."""
        return (self.x, self.y)



    def __repr__(self):
        return f"Position(x={self.x}, y={self.y})"
