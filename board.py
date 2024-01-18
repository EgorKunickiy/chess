from mixin import BoardValidationMixin
from player import Player
from figure import Figure

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

    def move(self, player: Player, string_from: str, string_to: str) -> None:
        coords_from = self.convert_coords(string_from)
        coords_to = self.convert_coords(string_to)

        if coords_to and coords_from:
            cell_first = self.cells[coords_from[1]][coords_from[0]]
            cell_second = self.cells[coords_to[1]][coords_to[0]]
        else:
            print('inncorrect coords')
            return

        if issubclass(type(cell_first), Figure):
            if cell_first.color == player.color:
                if cell_first.can_go(coords_from, coords_to):
                    if issubclass(type(cell_second), Figure):
                        if cell_second.color != player.color and cell_first.beat(coords_from, coords_to):
                            self.cells[coords_to[1]][coords_to[0]] = cell_first
                            self.cells[coords_from[1]][coords_from[0]] = '*'
                            return
                        else: 
                            print('you cant beat')
                    else:
                        self.cells[coords_to[1]][coords_to[0]] = cell_first
                        self.cells[coords_from[1]][coords_from[0]] = '*'
                        return 
                else: 
                    print('you cant go')
            else:
                print('it isnt your figure')
        else:
            print('it isnt figure')


if __name__ == '__main__':
    b = Board()
    b.print_board()
