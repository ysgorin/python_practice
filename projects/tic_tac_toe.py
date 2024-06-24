def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+\n\
|       |       |       |\n\
|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |\n\
|       |       |       |\n\
+-------+-------+-------+\n\
|       |       |       |\n\
|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |\n\
|       |       |       |\n\
+-------+-------+-------+\n\
|       |       |       |\n\
|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |\n\
|       |       |       |\n\
+-------+-------+-------+")

def make_list_of_free_fields(board):
#     The function browses the board and builds a list of all the free squares; 
#     the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    row_number = 1
    for row in board:
        column_number = 1
        for column in row:
            if type(column) == int:
                free_fields.append((row_number, column_number))
            column_number += 1
        row_number += 1
    return free_fields

# def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.

# def victory_for(board, sign):
#     The function analyzes the board's status in order to check if 
#     the player using 'O's or 'X's has won the game

# def draw_move(board):
#     The function draws the computer's move and updates the board.

board = [[1,2,3],[4,"X",6],[7,8,9]]

display_board(board)
print(make_list_of_free_fields(board))

# Your task is to write a simple program which
# pretends to play tic-tac-toe with the user. To
# make it all easier for you, we've decided to
# simplify the game. Here are our assumptions:
# * the computer (i.e., your program) should play
# the game using 'X's;
# * the user (e.g., you) should play the game
# using 'O's;
# * the first move belongs to the computer − it
# always puts its first 'X' in the middle of the
# board;
# * all the squares are numbered row by row
# starting with 1 (see the example session below
# for reference)
# * the user inputs their move by entering the
# number of the square they choose − the number
# must be valid, i.e., it must be an integer, it
# must be greater than 0 and less than 10, and it
# cannot point to a field which is already
# occupied;
# * the program checks if the game is over −
# there are four possible verdicts: the game
# should continue, the game ends with a tie, you
# win, or the computer wins;
# * the computer responds with its move and the
# check is repeated;
# * don't implement any form of artificial
# intelligence − a random field choice made by
# the computer is good enough for the game.

# Implement the following features:
# * the board should be stored as a three-element
# list, while each element is another
# three-element list (the inner lists represent
# rows) so that all of the squares may be
# accessed using the following syntax:
# board[row][column]
# * each of the inner list's elements can contain
# 'O', 'X', or a digit representing the square's
# number (such a square is considered free)
# * the board's appearance should be exactly the
# same as the one presented in the example.
# * implement the functions defined for you in
# the editor.
# * Drawing a random integer number can be done
# by utilizing a Python function called
# randrange(). The example program below shows
# how to use it (the program prints ten random
# numbers from 0 to 8).