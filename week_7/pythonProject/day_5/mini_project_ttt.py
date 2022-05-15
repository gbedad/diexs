# Tic Tac Toe game
import random


def get_new_board():
    board = []
    for x in range(15):
        board.append([]) # rather than appending empty list then append each time, you can create and add to it and just at the end add it to the borad
        for y in range(5):
            if x == 5 or x == 9: # you can make it more clean by: if x in [5, 9]
                board[x].append('|')
            elif (x == 5 or x == 9) and (y == 1 or y == 3):
                board[x].append('|')
            elif (y == 1 or y == 3) and (2 <= x < 5 or 6 <= x < 9 or 10 <= x < 13):
                board[x].append('-')
            else:
                board[x].append(' ')
    return board

# to create new borad, which a fixed size we can simplify the display by:
# board = {'7': ' ' , '8': ' ' , '9': ' ' ,
#             '4': ' ' , '5': ' ' , '6': ' ' ,
#             '1': ' ' , '2': ' ' , '3': ' ' }

# def get_new_board():
#     print(board['7'] + '|' + board['8'] + '|' + board['9'])
#     print('-+-+-')
#     print(board['4'] + '|' + board['5'] + '|' + board['6'])
#     print('-+-+-')
#     print(board['1'] + '|' + board['2'] + '|' + board['3'])
    
def display_top_bottom():
    print("*" * 17)


def draw_board(board):
    print("TIC TAC TOE")
    display_top_bottom()
    for row in range(5):
        board_row = ''
        for column in range(15):
            board_row += board[column][row]
        print(f"*{board_row}*")
    display_top_bottom()


def redefine_pos_y(y):
    if y == 1:
        return 0
    if y == 2:
        return 2
    if y == 3:
        return 4


def redefine_pos_x(x):
    if x == 1:
        return 3
    if x == 2:
        return 7
    if x == 3:
        return 11


def player_input():
    input_row = int(input("Enter row: "))
    input_column = int(input("Enter column: "))
    while input_column not in [1, 2, 3] or input_row not in [1, 2, 3]: # rather than creating the input twice you can create flag like ivalid_input which start with true and once you get a vaild input it will be true
        print("Not in board, retry")
        input_row = int(input("Enter row: "))
        input_column = int(input("Enter column: "))
    return input_column, input_row


def player_move(x, y, previous_moves):
    board = get_new_board()
    for x, y, p in previous_moves:
        board[redefine_pos_x(x)][redefine_pos_y(y)] = p
    return board


def check_if_in_previous_moves(prev, x, y, player):
    if [x, y, player] in prev:
        prev.remove([x, y, player])
        print(f"This move has already been made")


def check_win(prev, player):
    moves = filter(lambda s: s[2] == player, prev)
    list_moves = list(moves)
    print(list_moves)
    wins = [[[1, 1, player], [2, 2, player], [3, 3, player]],
            [[1, 1, player], [2, 1, player], [3, 1, player]],
            [[1, 1, player], [1, 2, player], [1, 3, player]],
            [[2, 1, player], [2, 2, player], [2, 3, player]],
            [[3, 1, player], [3, 2, player], [3, 3, player]],
            [[1, 3, player], [2, 3, player], [3, 3, player]],
            [[1, 3, player], [2, 2, player], [3, 1, player]],
            [[1, 2, player], [2, 2, player], [3, 2, player]],
            ]
    for item in wins:
        if all(element in list_moves for element in item):
            return True


def define_random_player():
    player_to_start = random.choice(["X", "O"])
    return player_to_start


def play():
    play_again = True
    player = define_random_player()
    while play_again:
        print(f"Player {player}'s turn...")
        x, y = player_input()
        check_if_in_previous_moves(previous_moves_params, x, y, player)
        previous_moves_params.append([x, y, player])
        check = check_win(prev=previous_moves_params, player=player)
        new_board = player_move(redefine_pos_x(x), redefine_pos_y(y), previous_moves_params)
        draw_board(new_board)
        # print(previous_moves_params)
        if check:
            print(f"Player {player} is the winner")
            play_again = False
        elif len(previous_moves_params) >= 9:
            play_again = False
            print("No winner in this game, tie")
        if player == 'X':
            player = 'O'
        else:
            player = 'X'


previous_moves_params = []
player_moves = []
new_board = get_new_board()
draw_board(new_board)
play()

# TODO check if input in list_moves, reject if yes

