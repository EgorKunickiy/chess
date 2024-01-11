from color import Color
from builders import (
    Builder,
    Player,
    Board)


class Director:

    def __init__(self) -> None:
        self.board_builder = None
        self.player_builder = None

    def set_builders(self, builder_1: Builder, builder_2: Builder) -> None:
        self.board_builder = builder_2
        self.player_builder = builder_1

    def generate_players(self) -> tuple(Player, Player):
        self.player_builder.generate_figures()
        self.player_builder.set_color(Color.white)

        player1 = self.player_builder.product()
        self.player_builder.set_color(Color.black)
        self.player_builder.generate_figures()
        player2 = self.player_builder.product()
        return (player1, player2)

    def generate_board(self, player_white: Player, player_black: Player) -> Board:
        self.board_builder.arrangement_of_figures(self.player1)
        self.board_builder.arrangement_of_figures(self.player2)
        return self.board_builder.product()
