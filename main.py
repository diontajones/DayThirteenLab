import checkers


def game():
    size = int(input("Enter the size of the board: "))
    board = checkers.build_board(size)
    print(board)
    print("Number of Empty cells:", checkers.get_count(board, 'Empty'))
    print("Number of Red cells:", checkers.get_count(board, 'Red'))
    print("Number of Black cells:", checkers.get_count(board, 'Black'))


if __name__ == '__main__':
    game()

