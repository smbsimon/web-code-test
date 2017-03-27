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


if __name__ == "__main__":
    new_board = Board()
    new_board.draw_board()


# up next: implementation of game logic

# ask human player for first move input
# for each machine move, check first to see if machine can win:
    # if yes, place machine move to win
    # if no, check to see if human can win
        # if human can win, block human win
        # else... make a random move? corners are strong, which means:

# board might need more specific breakdowns:
    # center, corners, sides
