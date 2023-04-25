import random

class SudokuBoard:
    def __init__(self):
        self.generate_board()
        self.clean_rows()
        self.clean_columns()
        self.clean_blocks()

    def generate_board(self):
        for row in self.grid:
            for col in range(0, 9):
                row[col] = random.randint(0, 9)

    def clean_rows(self):
        # Remove duplicate numbers from each row
        for row in self.grid:
            existing_numbers = []
            for row_idx in range(0, 9):
                if row[row_idx] not in existing_numbers:
                    existing_numbers.append(row[row_idx])
                else:
                    row[row_idx] = 0

    def clean_columns(self):
        # Determine columns
        columns = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
        for row in self.grid:
            for row_idx in range(0, 9):
                columns.get(row_idx).append(row[row_idx])

        # Remove duplicate numbers from each column
        for col_idx in range(len(columns)):
            cur_col = columns.get(col_idx)
            existing_numbers = []
            for row_idx in range(len(cur_col)):
                if cur_col[row_idx] not in existing_numbers:
                    existing_numbers.append(cur_col[row_idx])
                else:
                    self.grid[row_idx][col_idx] = 0

    def clean_blocks(self):
        # Remove duplicates from each block (nonet)
        for row_idx in range(0, 9):
            for col_idx in range(0, 9):
                cur_num = self.grid[row_idx][col_idx]
                block_x = (col_idx // 3) * 3
                block_y = (row_idx // 3) * 3
                count = 0
                for i in range(0, 3):
                    for j in range(0, 3):
                        if self.grid[block_y + i][block_x + j] != 0:
                            if self.grid[block_y + i][block_x + j] == cur_num:
                                count += 1
                            if count > 1:
                                self.grid[block_y + i][block_x + j] = 0
