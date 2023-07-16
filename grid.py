from tools import create_zeros_grid


class Grid:
    def __init__(self, matrix):
        self.matrix = matrix
        self.width = len(matrix[0])
        self.height = len(matrix)

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __repr__(self):
        return f"Grid({self.matrix})"

    def __str__(self):
        output_str = ""
        for row in self.matrix:
            output_str += str(row) + "\n"
        return output_str

    def does_cell_live(self, current_state, neighbour_count):
        if current_state:  # alive
            if neighbour_count < 2:
                return False
            elif neighbour_count > 3:
                return False
            else:
                return True
        else:  # dead
            if neighbour_count == 3:
                return True
            else:
                return False

    def get_neighbour_count(self, cell_row, cell_col):
        neighbour_count = 0
        for i in range(cell_col - 1, cell_col + 1 + 1):
            for j in range(cell_row - 1, cell_row + 1 + 1):
                if i == cell_col and j == cell_row:
                    continue
                if i not in range(self.width):
                    continue
                if j not in range(self.height):
                    continue
                neighbour_count += self.matrix[j][i]

        return neighbour_count

    def get_next_cell_state(self, cell_row, cell_col):
        current_state = self.matrix[cell_row][cell_col]
        neighbour_count = self.get_neighbour_count(cell_row, cell_col)
        new_cell_state = int(self.does_cell_live(current_state, neighbour_count))
        return new_cell_state

    def evolve(self):
        new_matrix_state = create_zeros_grid(self.width, self.height)
        for row_index in range(self.height):
            for col_index in range(self.width):
                new_cell_state = self.get_next_cell_state(row_index, col_index)
                new_matrix_state[row_index][col_index] = new_cell_state

        self.matrix = new_matrix_state
