# First milestone project: Tic Tac Toe
# The Complete Python Bootcamp from zero to hero by Jose Portilla
# Made bo me according to the steps from the course
# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/04-Milestone%
# 20Project%20-%201/02-Milestone%20Project%201%20-%20Walkthrough%20Steps%20Workbook.ipynb

from random import randint

# Task 1: Print out a board.


def display_board(board):

    print('\n')
    print(' ' + board[7] + '|' + board[8] + '|' + board[9])
    print('-------')
    print(' ' + board[4] + '|' + board[5] + '|' + board[6])
    print('-------')
    print(' ' + board[1] + '|' + board[2] + '|' + board[3])


# Task 2: Player input and assign a marker as 'X' or 'O'.

def player_input():

    signs_list = ['X', 'O']
    marker = ''

    while marker not in signs_list:
        marker = input('Player1 choose (X/O): ').upper()

        if marker == 'X':
            return 'X', 'O'
        elif marker == 'O':
            return 'O', 'X'
        else:
            print('Invalid choice. Try again.')


# Task 3: takes in the board a marker ('X' or 'O') in a desired position (number 1-9).

def place_marker(board, marker, position):

    board[position] = marker


# Task 4: takes in a board with a marked (X or O) and then checks to see if that mark has won.

def win_check(board, mark):

    # WIN TIC TAC TOE
    # ALL ROWS, and check to see if they all share the same marker?
    return(board[1] == board[2] == board[3] == mark) or \
          (board[4] == board[5] == board[6] == mark) or \
          (board[7] == board[8] == board[9] == mark) or \
          (board[1] == board[4] == board[7] == mark) or \
          (board[2] == board[5] == board[8] == mark) or \
          (board[3] == board[6] == board[9] == mark) or \
          (board[1] == board[5] == board[9] == mark) or \
          (board[3] == board[5] == board[7] == mark)


# Task 5: Which player goes first using randint function


def choose_first():
    number = randint(0, 1)
    if number == 0:
        return 'player1'
    else:
        return 'player2'


# Task 6: Is space on the board is freely available.

def space_check(board, position):
    return board[position] == ' '


# Step 7: Check if the board is full and returns a boolean value.


def is_full(board):
    n = 0
    for element in board:
        if element != ' ':
            n += 1
    if n == 9:
        return True
    else:
        return False


# Task 8: Ask for a player's next position (as a number 1-9)
# and use space_check to check if it's a free position.


def player_choice(board):

    while True:
        position = int(input('Choose your next position: (1-9) '))
        if position not in range(1,10):
            print('This position is prohibited. Choose one from 1 to 9')
        elif space_check(board, position) == False:
            print('This position is already occupied')
        else:
            return position
            break



# Step 9: Ask the player if they want to play again and returns a boolean
# True if they do want to play again.

def next_game():
    once_again = ''
    yn_list = ['Y', 'N']
    while once_again not in yn_list:
        once_again = input('Do you want to play again? (Y/N)').upper()
    if once_again == 'Y':
        return True
    else:
        return False


# Task 10: Here comes the hard part! Use while loops and the functions you've made to run the game!


print('TIC TAC TOE GAME')
print('\n')

# PLAY THE GAME

## SET EVERYTHING UP (BOARD, WHOS FIRST, CHOOSE MARKERS X, O )
the_board = [' ']*10
player1_marker, player2_marker = player_input()
turn = choose_first()
print(turn + ' go first')

while True:

    play_game = input('ready to play? y or n? ')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    ## GAME PLAY

    while game_on:

        if turn == 'player1':
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            print(position)
            # Place a marker on the position
            place_marker(the_board, player1_marker, position)
            display_board(the_board)

            # Check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!!')
                game_on = False
            elif is_full(the_board):
                display_board(the_board)
                print("TIE GAME!")
                game_on = False
            else:
                turn = 'player2'


### PLAYER ONE TURN

        else:
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place a marker on the position
            place_marker(the_board, player2_marker, position)
            display_board(the_board)

            # Check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!!')
                game_on = False
            elif is_full(the_board):
                display_board(the_board)
                print("TIE GAME!")
                game_on = False
            else:
                turn = 'player1'

    if not next_game():
        break

