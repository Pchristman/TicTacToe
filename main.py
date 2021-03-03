import random


def display_board(board):
    print("\n" * 100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():
    marker = ' '

    while marker != 'X' and marker != "O":
        marker = input("Player 1, choose X or O: ")

    player1 = marker
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    return player1, player2


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    won_game = False
    # CHECK TO SEE IF THERES A WIN IN THE ROWS
    if board[1] == mark and board[2] == mark and board[3] == mark:
        won_game = True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        won_game = True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        won_game = True
    # CHECK THE COLUMNS NOW
    elif board[7] == mark and board[4] == mark and board[1] == mark:
        won_game = True
    elif board[8] == mark and board[5] == mark and board[2] == mark:
        won_game = True
    elif board[9] == mark and board[6] == mark and board[3] == mark:
        won_game = True
    # NOW CHECKING DIAGONALS
    elif board[9] == mark and board[5] == mark and board[1] == mark:
        won_game = True
    elif board[7] == mark and board[5] == mark and board[3] == mark:
        won_game = True
    else:
        pass

    return won_game


def choose_first():
    first = random.randint(1, 2)
    if first == 1:
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in range(1, 10) and not space_check(board, position):
        position = int(input("Choose a position: (1-9) "))
    return position


def replay():
    choice = "wrong"

    while choice not in ["Y", "N"]:
        choice = input("Would you like to play again? Y or N ")
        if choice not in ["Y", "N"]:
            print("\n" * 100)
            print("Sorry I didn't understand; Try again")

    if choice == "Y":
        return True
    else:
        return False


print("Welcome to Tic Tac Toe!")

# WHILE LOOP TO KEEP RUNNING THE GAME
while True:

    # PLAY THE GAME
    # SET EVERYTHING UP (BOARD, WHO'S FIRST, CHOOSE MARKERS X, O)
    game_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(f'{turn} will go first')

    play_game = input("Ready to play? y or n ")

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "Player 1":
            display_board(game_board)
            index = player_choice(game_board)
            place_marker(game_board, player1_marker, index)
            if win_check(game_board, player1_marker):
                display_board(game_board)
                print("Player 1 won the game!")
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print("There is a tie!")
                    game_on = False
                else:
                    turn = "Player 2"
        else:
            display_board(game_board)
            index = player_choice(game_board)
            place_marker(game_board, player2_marker, index)
            if win_check(game_board, player2_marker):
                display_board(game_board)
                print("Player 2")
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print("There is a tie")
                    game_board = False
                else:
                    turn = "Player 1"

    if not replay():
        break

# BREAK OUT OF THE WHILE LOOP ON replay()
