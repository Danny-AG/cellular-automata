import time
# TODO - install numpy and use arrays instead of lists when have internet
from grid import Grid
from tools import import_data_from_excel


def simulate(grid):
    current_grid = grid
    while True:
        print(current_grid)
        time.sleep(1)
        current_grid.evolve()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init_data_path = "~/git/cellular-autonama/input/gs_2_10x10_glider.xlsx"

    excel_data = import_data_from_excel(init_data_path)
    initial_grid = Grid(excel_data)
    simulate(initial_grid)
