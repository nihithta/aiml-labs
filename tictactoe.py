import numpy as np

# Constants for players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Initialize the game board
board = np.full((3, 3), EMPTY)

def print_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def is_winner(player):
    return any(np.all(board[i] == player) for i in range(3)) or \
           any(np.all(board[:, j] == player) for j in range(3)) or \
           np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player)

def is_draw():
    return np.all(board != EMPTY)

def minimax(is_maximizing):
    if is_winner(PLAYER_O):
        return 1
    if is_winner(PLAYER_X):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -np.inf
        for i, j in zip(*np.where(board == EMPTY)):
            board[i, j] = PLAYER_O
            score = minimax(False)
            board[i, j] = EMPTY
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = np.inf
        for i, j in zip(*np.where(board == EMPTY)):
            board[i, j] = PLAYER_X
            score = minimax(True)
            board[i, j] = EMPTY
            best_score = min(best_score, score)
        return best_score

def best_move():
    best_score = -np.inf
    move = (-1, -1)
    for i, j in zip(*np.where(board == EMPTY)):
        board[i, j] = PLAYER_O
        score = minimax(False)
        board[i, j] = EMPTY
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

def play():
    current_player = PLAYER_X
    while True:
        print_board()
        if current_player == PLAYER_X:
            row, col = map(int, input("Your move (row and column): ").split())
        else:
            row, col = best_move()
            print(f"AI chose: {row} {col}")

        if board[row, col] == EMPTY:
            board[row, col] = current_player
            if is_winner(current_player):
                print_board()
                print(f"{current_player} wins!")
                break
            if is_draw():
                print_board()
                print("It's a draw!")
                break
            current_player = PLAYER_X if current_player == PLAYER_O else PLAYER_O
        else:
            print("Invalid move, try again.")

if __name__ == "__main__":
    play()
