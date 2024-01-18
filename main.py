from builders import PlayerBuilder, BoardBuilder
from director import Director
from board import Board
from player import Player


def get_player_coord(player: Player) -> str:
    print(player.color.value)
    own_coords = input('coords your figure: ')
    new_coords = input('Where: ')

    return own_coords, new_coords


def mainloop(player_white: Player, player_black: Player, board: Board) -> None:
    turn = 1
    while True:
        board.print_board()
        if turn % 2 == 1:
            current_player = player_white
        else:
            current_player = player_black

        own_c, new_c = get_player_coord(current_player)
        board.move(current_player, own_c, new_c)
        turn += 1


def main():
    director = Director()
    player_builder = PlayerBuilder()
    board_builder = BoardBuilder()
    director.set_builders(player_builder, board_builder)

    player_white, player_black = director.generate_players()
    board = director.generate_board(player_white, player_black)
    mainloop(player_white, player_black, board)


if __name__ == '__main__':
    main()
