class Board():

    def __init__(self, first_row, second_row, third_row):
        """Initialize board with three rows"""
        self.first_row = first_row
        self.second_row = second_row
        self.third_row = third_row

    def draw_board(self):
        """Create a new instance of the board"""
        print (self.first_row + '\n' + self.second_row + '\n' + self.third_row)

new_board = Board('[_]' * 3, '[_]' * 3, '[_]' * 3)
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
    # board construction might be better off in a list? that way i can query & insert by index...
