import numpy as np


def build_board(size):
    board = np.random.choice(['Empty', 'Red', 'Black'], size=(size, size))
    return board


def get_count(board, item):
    count = np.count_nonzero(board == item)
    return count


if __name__ == '__main__':
    print("This file is not intended to be run as a main.")
