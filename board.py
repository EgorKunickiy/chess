from mixin import BoardValidationMixin

ROW_COUNT = 8


class Board(BoardValidationMixin):

    def __init__(self) -> None:
        self.cells = [['*' for i in range(8)] for j in range(8)]

    def print_board(self) -> None:
        letters = "  A B C D E F G H"
        print(letters)
        for row in range(ROW_COUNT):
            print(row+1, *self.cells[row], row+1)
        print(letters)


if __name__ == '__main__':
    b = Board()
    b.print_board()
