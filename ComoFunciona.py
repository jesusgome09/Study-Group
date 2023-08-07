def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_eval = -float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                eval = minimax(board, 0, False)
                board[i][j] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

def tictactoe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        if current_player == 'X':
            row = int(input(f"Player {current_player}, choose a row (0, 1, or 2): "))
            col = int(input(f"Player {current_player}, choose a column (0, 1, or 2): "))
        else:
            print("Computer's turn...")
            row, col = find_best_move(board)

        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("That cell is already occupied. Try again.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            if current_player == 'X':
                print(f"Player {current_player} wins!")
            else:
                print("Computer wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tictactoe()

