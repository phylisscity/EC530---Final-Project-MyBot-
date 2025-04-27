
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
        old_x, old_y = self.x, self.y  # Save previous coordinates

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

        # Check if new position is still inside grid
        if not self.is_within_bounds():
            # Undo move and raise error
            self.x, self.y = old_x, old_y
            raise ValueError("Move would go out of bounds.")



    def get_coords(self):
        """Return the current (x, y) position as a tuple."""
        return (self.x, self.y)



    def __repr__(self):
        return f"Position(x={self.x}, y={self.y})"
    
    
    def is_within_bounds(self):
    
        """
        Check if the current position is within the grid boundaries. 10x10

        Returns:
            True if within (0,0) to (GRID_WIDTH-1, GRID_HEIGHT-1), else False.
        """
        return 0 <= self.x < GRID_WIDTH and 0 <= self.y < GRID_HEIGHT

