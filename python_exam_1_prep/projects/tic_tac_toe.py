from random import randrange
from time import sleep

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(("+"+("-"*7))*3+"+\n\
"+("|"+(" "*7))*3+"|\n\
|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |\n\
"+("|"+(" "*7))*3+"|\n\
"+("+"+("-"*7))*3+"+\n\
"+("|"+(" "*7))*3+"|\n\
|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |\n\
"+("|"+(" "*7))*3+"|\n\
"+("+"+("-"*7))*3+"+\n\
"+("|"+(" "*7))*3+"|\n\
|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |\n\
"+("|"+(" "*7))*3+"|\n\
"+("+"+("-"*7))*3+"+")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    valid_moves = []
    for field in make_list_of_free_fields(board):
        if field == (1,1):
            valid_moves.append(1)
        elif field == (1,2):
            valid_moves.append(2)
        elif field == (1,3):
            valid_moves.append(3)
        elif field == (2,1):
            valid_moves.append(4)
        elif field == (2,2):
            valid_moves.append(5)
        elif field == (2,3):
            valid_moves.append(6)
        elif field == (3,1):
            valid_moves.append(7)
        elif field == (3,2):
            valid_moves.append(8)
        elif field == (3,3):
            valid_moves.append(9)
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            # Reject any integer inputs that are not between 1-9
            if move < 1 or move > 9:
                raise ValueError("Invalid move. Please choose a number between 1 and 9.")
            if move not in valid_moves:
                raise ValueError("Invalid move. Please choose a free space.")
            break
        except:
            print("Invalid input. Please enter a number between 1 and 9.")
    for row in range(3):
        for column in range(3):
            if board[row][column] == move:
                board[row][column] = 'O'
    return board

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

def victory_for(board, sign):
#     The function analyzes the board's status in order to check if 
#     the player using 'O's or 'X's has won the game
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return True
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return True
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    return False

def draw_move(board):
#     The function draws the computer's move and updates the board.
    valid_moves = []
    for field in make_list_of_free_fields(board):
        if field == (1,1):
            valid_moves.append(1)
        elif field == (1,2):
            valid_moves.append(2)
        elif field == (1,3):
            valid_moves.append(3)
        elif field == (2,1):
            valid_moves.append(4)
        elif field == (2,2):
            valid_moves.append(5)
        elif field == (2,3):
            valid_moves.append(6)
        elif field == (3,1):
            valid_moves.append(7)
        elif field == (3,2):
            valid_moves.append(8)
        elif field == (3,3):
            valid_moves.append(9)
    while True:
        move = randrange(1,9)
        if move in valid_moves:
            for row in range(3):
                for column in range(3):
                    if board[row][column] == move:
                        board[row][column] = 'X'
            break
    return board                

def tie_game(board):
    for row in board:
        for cell in row:
            if cell != 'X' and cell != 'O':
                return False
    return True    

print("Let's play Tic Tac Toe.\n\
You are 'O' and the computer is 'X'\n\
To move, choose the number of a free space.")

board = [[1,2,3],[4,5,6],[7,8,9]]
display_board(board)
sleep(1)

while True:
    enter_move(board)
    display_board(board)
    if victory_for(board, "O") == True:
        print("You won!")
        break
    elif tie_game(board) == True:
        print("Tie game.")
        break
    sleep(1)
    draw_move(board)
    display_board(board)
    if victory_for(board, "X") == True:
        print("The computer won. :( ")
        break
    elif tie_game(board) == True:
        print("Tie game.")
        break
    sleep(1)