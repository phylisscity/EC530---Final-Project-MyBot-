
#grid
from MyBot.config import GRID_WIDTH, GRID_HEIGHT
from MyBot.world.grid import is_within_bounds  



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
        elif direction == "up-right":
            self.y += 1
            self.x += 1
        elif direction == "up-left":
            self.y += 1
            self.x -= 1
        elif direction == "down-right":
            self.y -= 1
            self.x += 1
        elif direction == "down-left":
            self.y -= 1
            self.x -= 1
        else:
            raise ValueError(f"Invalid direction: {direction}")


        # Check if new position is still inside grid
        if not is_within_bounds(self.x, self.y, GRID_WIDTH, GRID_HEIGHT):
            
            # Undo move and raise error
            self.x, self.y = old_x, old_y
            raise ValueError("Move would go out of bounds.")



    def get_coords(self):
        """Return the current (x, y) position as a tuple."""
        return (self.x, self.y)



    def __repr__(self):
        return f"Position(x={self.x}, y={self.y})"
    
    
