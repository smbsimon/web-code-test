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

    def can_win():
        """Show options for winning combinations"""
        winning_combos = [
            [board[0][0], board[0][1], board[0][2]],
            [board[1][0], board[1][1], board[1][2]],
            [board[2][0], board[2][1], board[2][2]],
            [board[0][0], board[1][0], board[2][0]],
            [board[0][1], board[1][1], board[2][1]],
            [board[0][2], board[1][2], board[2][2]],
            [board[0][0], board[1][1], board[2][2]],
            [board[0][2], board[1][1], board[2][0]],
        ]
        return winning_combos

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

# this should all be separated out into a play class...
