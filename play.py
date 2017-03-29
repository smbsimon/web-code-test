from board import Board

class PlayGame():
    """Code for executing a run of the game"""

    def start_game(self):
        """Creates a new instance of Tic Tac Toe"""
        print "Welcome to Tic Tac Toe. Are you ready to (p)lay or do you need some (h)elp?\n"
        instructions = raw_input()

        if instructions == "p":
            print "All right! You make the first move. Enter the index number of your choice. The board ranges from 1-9, upper left to bottom right."
            new_board = Board()
            new_board.draw_board()
        elif instructions == "h":
            print "You really don't know how to play Tic Tac Toe?"
        else:
            print "Sorry. I didn't understand that."

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


if __name__ == "__main__":
    tictactoe = PlayGame()
    tictactoe.start_game()


# up next: implementation of game logic

# draw_board() shouldn't be called within the instructions if statement
# users should be able to call for instructions at any point without losing state of the board

# ask human player for first move input
# for each machine move, check first to see if machine can win:
    # if yes, place machine move to win
    # if no, check to see if human can win
        # if human can win, block human win
        # else... make a random move? corners are strong, which means:
