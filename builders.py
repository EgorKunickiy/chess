from abc import ABC
from player import Player
from color import Color
from board import Board
from figure import (
    Pawn,
    Bishop,
    Horse,
    Rook,
    Queen,
    King)


class Builder(ABC):
    pass


class PlayerBuilder(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Player()

    def product(self) -> Player:
        product = self._product
        self.reset()
        return product

    def set_color(self, color: Color) -> None:
        self._product.color = color
        for figure in self._product.all_figures:
            figure.set_color(color)

    def generate_figures(self) -> None:
        pawn_1 = Pawn()
        pawn_2 = Pawn()
        pawn_3 = Pawn()
        pawn_4 = Pawn()
        pawn_5 = Pawn()
        pawn_6 = Pawn()
        pawn_7 = Pawn()
        pawn_8 = Pawn()
        knight_1 = Horse()
        knight_2 = Horse()
        bishop_1 = Bishop()
        bishop_2 = Bishop()
        rook_1 = Rook()
        rook_2 = Rook()
        queen = Queen()
        king = King()

        self._product.all_figures.append(pawn_1)
        self._product.all_figures.append(pawn_2)
        self._product.all_figures.append(pawn_3)
        self._product.all_figures.append(pawn_4)
        self._product.all_figures.append(pawn_5)
        self._product.all_figures.append(pawn_6)
        self._product.all_figures.append(pawn_7)
        self._product.all_figures.append(pawn_8)
        self._product.all_figures.append(knight_1)
        self._product.all_figures.append(knight_2)
        self._product.all_figures.append(bishop_1)
        self._product.all_figures.append(bishop_2)
        self._product.all_figures.append(rook_1)
        self._product.all_figures.append(rook_2)
        self._product.all_figures.append(queen)
        self._product.all_figures.append(king)


class BoardBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Board()

    def product(self) -> Player:
        product = self._product
        self.reset()
        return product

    def arrangement_of_figures(self, player: Player) -> None:
        if player.color == Color.white:
            for figure in player.all_figures:

                name = figure.get_full_name()
                match name:
                    case 'Pawn':
                        for col in range(8):
                            if self._product.cells[1][col]:
                                self._product.cells[1][col] = figure

                    case 'Bishop':
                        if self._product.cells[0][2] == '*':
                            self._product.cells[0][2] = figure
                        else:
                            self._product.cells[0][5] = figure

                    case 'Horse':
                        if self._product.cells[0][1] == '*':
                            self._product.cells[0][1] = figure
                        else:
                            self._product.cells[0][6] = figure

                    case 'Rook':
                        if self._product.cells[0][0] == '*':
                            self._product.cells[0][0] = figure
                        else:
                            self._product.cells[0][7] = figure

                    case 'Queen':
                        self._product.cells[0][3] = figure

                    case 'King':
                        self._product.cells[0][4] = figure

        else:
            for figure in player.all_figures:

                name = figure.get_full_name()
                match name:
                    case 'Pawn':
                        for col in range(8):
                            if self._product.cells[6][col] == "*":
                                self._product.cells[6][col] = figure

                    case 'Bishop':
                        if self._product.cells[7][2] == '*':
                            self._product.cells[7][2] = figure
                        else:
                            self._product.cells[7][5] = figure

                    case 'Horse':
                        if self._product.cells[7][1] == '*':
                            self._product.cells[7][1] = figure
                        else:
                            self._product.cells[7][6] = figure

                    case 'Rook':
                        if self._product.cells[7][0] == '*':
                            self._product.cells[7][0] = figure
                        else:
                            self._product.cells[7][7] = figure

                    case 'Queen':
                        self._product.cells[7][3] = figure

                    case 'King':
                        self._product.cells[7][4] = figure


if __name__ == '__main__':
    build_p = PlayerBuilder()
    build_p.generate_figures()
    build_p.set_color(Color.white)
    player1 = build_p.product()

    build_p.generate_figures()
    build_p.set_color(Color.black)
    player2 = build_p.product()
    build_b = BoardBuilder()
    build_b.arrangement_of_figures(player1)
    build_b.arrangement_of_figures(player2)
    board = build_b.product()
    board.print_board()
