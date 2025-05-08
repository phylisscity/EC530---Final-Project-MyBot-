import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#forportability

from MyBot.movement.move import Position


def test_position_movement():
    pos = Position()
    pos.move("up")
    assert pos.get_coords() == (0, 1)

    pos.move("right")
    assert pos.get_coords() == (1, 1)

    pos.move("down")
    assert pos.get_coords() == (1, 0)

    pos.move("left")
    assert pos.get_coords() == (0, 0)

    print("[PASS] Position movement test passed.")


if __name__ == "__main__":
    test_position_movement()
