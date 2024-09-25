def is_valid(board, row, col, num):
    # Check if num is not in the current row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if num is not in the current 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_location(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def sudoku_solver(board):
    empty_location = find_empty_location(board)
    
    # If there is no empty location, the board is solved
    if not empty_location:
        return True

    row, col = empty_location

    for num in range(1, 10):  # Numbers 1-9
        if is_valid(board, row, col, num):
            board[row][col] = num  # Place the number
            
            if sudoku_solver(board):
                return True  # If successful, return True
            
            board[row][col] = 0  # Reset on backtrack

    return False  # Trigger backtracking

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

# Example Sudoku puzzle (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if sudoku_solver(sudoku_board):
    print("Sudoku puzzle solved successfully!")
    print_board(sudoku_board)
else:
    print("No solution exists.")
