import pandas as pd


def create_zeros_grid(width: int, height: int) -> [[]]:
    return [[0 for i in range(width)] for j in range(height)]


def import_data_from_excel(path: str) -> [[]]:
    """
    Import data from Excel spreadsheet.

    :param path:
    :return: 2D list of alive/dead cells
    """

    df = pd.read_excel(path)
    return df.values.tolist()

