
grid = [
        [0, 0, 0, 0, 0, 8, 0, 4, 6],
        [0, 0, 0, 0, 0, 4, 0, 3, 0],
        [0, 0, 0, 9, 7, 2, 0, 0, 0],
        [2, 0, 7, 0, 0, 0, 4, 0, 0],
        [9, 0, 0, 8, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 4, 5, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 9, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 5, 1, 0]
    ]

def solve_puzzle(grid):
    # Base case: grid (board) is filled
    if not find_empty(grid):
        return True

    # Loop through the 2-d list
    for row_idx in range(0, len(grid)):
        for col_idx in range(0, len(grid)):
            if grid[row_idx][col_idx] == 0:
                # A 0 (zero) means the position is empty
                # Valid numbers in Sudoku are: 1 - 9
                for num in range(1, 10):
                    if possible_solution(grid, row_idx, col_idx, num):
                        # Possible solution found, set current position to current number
                        grid[row_idx][col_idx] = num
                        # Recursive call
                        if solve_puzzle(grid):
                            return True
                        # Reset current position
                        grid[row_idx][col_idx] = 0
                # No possible solution found at current position, backtrack
                return False

def find_empty(grid):
    for row_idx in range(len(grid)):
        for col_idx in range(len(grid)):
            if grid[row_idx][col_idx] == 0:
                return True

    return False

def possible_solution(grid, row, col, num):
    # The current row cannot contain the number
    for col_idx in range(0, 9):
        if grid[row][col_idx] == num:
            return False

    # The current column cannot contain the number
    for row_idx in range(0, 9):
        if grid[row_idx][col] == num:
            return False

    # The current block (nonet; 3x3 sub-block) cannot contain the number
    block_x = (col // 3) * 3
    block_y = (row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[block_y + i][block_x + j] == num:
                return False

    # No rules broken, number is a possible solution
    return True

def print_board(grid):
    print("-------------------------")
    row_count = 0
    for row in grid:
        row_count += 1
        print("|", end=" ")
        col_count = 0
        for col in row:
            col_count += 1
            print(col, end=" ")
            if col_count % 3 == 0 and col_count != 9:
                print("| ", end="")
            elif col_count == 9:
                print("|")
        if row_count % 3 == 0:
            print("-------------------------")

def main():
    # Print initial grid
    print("Starting grid:")
    print_board(grid)

    # Solve the Sudoku puzzle
    solve_puzzle(grid)

    # Print solved puzzle
    print("Solved grid:")
    print_board(grid)

main()
