#Final Project: Tic Tac Toe Game

board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False
def print_board(board):
    for i in range(3):
        print(" " + " | ".join(board[i]) + " ")
        if i < 2:
            print("---+---+---")
def take_input():
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            return row, col
        except ValueError:
            print("Invalid input! Please enter numbers only.")
def is_valid_move(board, row, col):
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    if board[row][col] != " ":
        return False
    return True
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def is_draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True
while not game_over:
    print_board(board)
    valid = False
    while not valid:
        row, col = take_input()
        if is_valid_move(board, row, col):
            valid = True
        else:
            print("Invalid move, try again.")
    board[row][col] = current_player
    if check_winner(board, current_player):
        print_board(board)
        print(current_player, "wins!")
        game_over = True
    elif is_draw(board):
        print_board(board)
        print("Game is a draw")
        game_over = True
    if not game_over:
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

