import checkers


def game():
    have_board = False
    while not have_board:
        print("Enter the size of the board - (min: 4, max: 16 ")
        size = int(input('> '))
        if size < 4 or size > 16:
            print('Please enter a number between 4 and 16.')
        else:
            have_board = True

    board = checkers.build_board(size)
    print(board)
    print("Number of Empty cells:", checkers.get_count(board, 'Empty'))
    print("Number of Red cells:", checkers.get_count(board, 'Red'))
    print("Number of Black cells:", checkers.get_count(board, 'Black'))


if __name__ == '__main__':
    game()

