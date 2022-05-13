# Tic Tac Toe game
def get_new_board():
    board = []
    for x in range(15):
        board.append([])
        for y in range(5):
            if x == 5 or x == 9:
                board[x].append('|')
            elif (x == 5 or x == 9) and (y == 1 or y == 3):
                board[x].append('|')
            elif (y == 1 or y == 3) and (2 <= x < 5 or 6 <= x < 9 or 10 <= x < 13):
                board[x].append('-')
            else:
                board[x].append(' ')
    return board


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


new_board = get_new_board()

draw_board(new_board)


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


def player_input(x, y, previous_moves):
    board = get_new_board()
    for x, y, p in previous_moves:
        board[redefine_pos_x(x)][redefine_pos_y(y)] = p
    return board


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

    if list_moves in wins:
        check = True
        # print(f"Player {player} is the winner")
        message = f"Player {player} is the winner"
        return check


def play():
    play_again = True
    player = 'X'
    while play_again:
        print(f"Player {player}'s turn...")
        input_row = int(input("Enter row: "))
        input_column = int(input("Enter column: "))
        previous_moves_params.append([input_column, input_row, player])
        check = check_win(prev=previous_moves_params, player=player)

        new_board = player_input(redefine_pos_x(input_column), redefine_pos_y(input_row), previous_moves_params)
        draw_board(new_board)
        if check == True:
            print(f"Player {player} is the winner")
            play_again = False
        else:
            print("Tie")
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        # print(player)


previous_moves_params = []
player_moves = []
play()


def player_input():
    pass
