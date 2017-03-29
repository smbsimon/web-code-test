class Board():

    def __init__(self):
        """Initialize board with three rows"""
        self.board = [
            ["_", "_", "_"],
            ["_", "_", "_"],
            ["_", "_", "_"],
        ]

    def draw_board(self):
        """Create a new instance of the board"""
        print self.board

    def is_center():
        """Check to see if spot is the center"""
        center = board[1][1]
        return center

    def is_corner():
        """Check to see if spot is a corner"""
        corners = [
            board[0][0], board[0][2], board[2][0], board[2][2]
        ]
        return corners

    def is_side():
        """Check to see if spot is a side"""
        sides = [
            board[0][1], board[1][0], board[1][2], board[2][1]
        ]
        return sides
