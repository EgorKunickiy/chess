from color import Color
from abc import ABC, abstractclassmethod


class Figure(ABC):

    def __init__(self) -> None:
        self.color = None
        self.symbol = None

    def get_full_name(self) -> str:
        return f"{self.__class__.__name__}"

    def __str__(self) -> str:
        return self.symbol

    @abstractclassmethod
    def set_color(self, color: Color) -> None:
        pass

    @abstractclassmethod
    def can_go(self, own_coords: tuple[int, int], new_coords: tuple[int, int]) -> bool:
        pass

    @abstractclassmethod
    def beat(self, own_coords: tuple[int, int], new_coords: tuple[int, int]) -> bool:
        pass


class Pawn(Figure):
    def __init__(self) -> None:
        super().__init__()
        self.first_step = True

    def can_go(self, own_coords: tuple[int, int], new_coords: tuple[int, int]) -> bool:
        if self.first_step:
            if own_coords[1] - 2 <= new_coords[1] <= own_coords[1] + 2:
                self.first_step = False
                return True
        else:
            if new_coords[1] == own_coords[1] + 1:
                return True
        return False

    def beat(self, own_coords: tuple[int, int], new_coords: tuple[int, int]) -> bool:
        if self.color == Color.black:
            if new_coords[1] == own_coords[1] - 1 \
            and (new_coords[0]-1 == own_coords[0] or new_coords[0]+1 == own_coords[0]):
                return True
        else:
            if new_coords[1] == own_coords[1] + 1 \
            and (new_coords[0]-1 == own_coords[0] or new_coords[0]+1 == own_coords[0]):
                return True

    def set_color(self, color: Color) -> None:
        self.color = color

        if self.color == Color.black:
            self.symbol = "\u2659"
        else:
            self.symbol = '\u265F'


class Bishop(Figure):
    def can_go(self, own_coords: tuple[int, int], new_coords: tuple[int, int]) -> bool:
        if (own_coords[0]+own_coords[1]) % 2 == (new_coords[0]+new_coords[1]) % 2 \
         and abs(own_coords[0]-new_coords[0]) == abs(own_coords[1]-new_coords[1]):
            return True
        return False

    def set_color(self, color: Color) -> None:
        self.color = color

        if self.color == Color.black:
            self.symbol = "\u2657"
        else:
            self.symbol = '\u265D'

    def beat(self, own_coords: tuple[int, int], new_coords: tuple[int, int]) -> bool:
        return True


class Horse(Figure):
    def can_go(self, own_coords: tuple[int, int], new_coords: tuple[int, int]) -> bool:
        if abs(own_coords[0] - new_coords[0]) == 1 and abs(own_coords[1] - new_coords[1]) == 2 \
         or abs(own_coords[0] - new_coords[0]) == 2 and abs(own_coords[1] - new_coords[1]) == 1:
            return True
        return False

    def set_color(self, color: Color) -> None:
        self.color = color

        if self.color == Color.black:
            self.symbol = "\u2658"
        else:
            self.symbol = '\u265E'

    def beat(self, own_coords: tuple[int, int], new_coords: tuple[int, int]) -> bool:
        return True


class Rook(Figure):
    def can_go(self, own_coords: tuple[int, int], new_coords: tuple[int, int]) -> bool:
        if own_coords[0] == new_coords[0] or own_coords[1] == new_coords[1]:
            return True
        return False

    def set_color(self, color: Color) -> None:
        self.color = color

        if self.color == Color.black:
            self.symbol = "\u2656"
        else:
            self.symbol = "\u265C"

    def beat(self, own_coords: tuple[int, int], new_coords: tuple[int, int]) -> bool:
        return True


class Queen(Figure):
    def can_go(self, own_coords: tuple[int, int], new_coords: tuple[int, int]) -> bool:
        if (own_coords[0]+own_coords[1]) % 2 == (new_coords[0]+new_coords[1]) % 2 \
            and abs(own_coords[0]-new_coords[0]) == abs(own_coords[1]-new_coords[1]) \
                or (own_coords[0] == new_coords[0] or own_coords[1] == new_coords[1]):
            return True
        return False

    def set_color(self, color: Color) -> None:
        self.color = color

        if self.color == Color.black:
            self.symbol = "\u2655"
        else:
            self.symbol = '\u265B'

    def beat(self, own_coords: tuple[int, int], new_coords: tuple[int, int]) -> bool:
        return True


class King(Figure):
    def can_go(self, own_coords: tuple[int, int], new_coords: tuple[int, int]) -> bool:
        if own_coords[0]-1 <= new_coords[0] <= own_coords[0]+1 \
         and own_coords[1]-1 <= new_coords[1] <= own_coords[1]+1:
            return True
        return False

    def set_color(self, color: Color) -> None:
        self.color = color

        if self.color == Color.black:
            self.symbol = "\u2654"
        else:
            self.symbol = '\u265A'

    def beat(self, own_coords: tuple[int, int], new_coords: tuple[int, int]) -> bool:
        return True


if __name__ == '__main__':
    p = Pawn()
    print(p)
