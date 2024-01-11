from color import Color


class Figure:

    def __init__(self) -> None:
        self.color = '\033[0m'

    def set_color(self, color: Color):
        if color == Color.white:
            self.color = '\033[31m'
        else:
            self.color = '\033[33m'

    def can_go(self, own_coords: tuple[int, int], new_coords: tuple[int, int]) -> True:
        pass

    def get_full_name(self):
        return f"{self.__class__.__name__}"

    def get_short_name(self):
        return f"{self.color}{self.__class__.__name__[0]}\033[0m"

    def __str__(self) -> str:
        return self.get_short_name()


class Pawn(Figure):
    def can_go(self, own_coords: tuple[int, int], new_coords: tuple[int, int]) -> True | False:
        if (own_coords[1] == new_coords[1] + 1):
            return True
        return False


class Bishop(Figure):
    def can_go(self, own_coords: tuple[int, int], new_coords: tuple[int, int]) -> True | False:
        if (own_coords[0]+own_coords[1]) % 2 == (new_coords[0]+new_coords[1]) % 2 \
         and abs(own_coords[0]-new_coords[0]) == abs(own_coords[1]-new_coords[1]):
            return True
        return False


class Horse(Figure):
    def can_go(self, own_coords: tuple[int, int], new_coords: tuple[int, int]) -> True | False:
        if abs(own_coords[0] - new_coords[0]) == 1 and abs(own_coords[1] - new_coords[1]) == 2 \
         or abs(own_coords[0] - new_coords[0]) == 2 and abs(own_coords[1] - new_coords[1]) == 1:
            return True
        return False


class Rook(Figure):
    def can_go(self, own_coords: tuple[int, int], new_coords: tuple[int, int]) -> True | False:
        if own_coords[0] == new_coords[0] or own_coords[1] == new_coords[1]:
            return True
        return False


class Queen(Figure):
    def can_go(self, own_coords: tuple[int, int], new_coords: tuple[int, int]) -> True | False:
        if (own_coords[0]+own_coords[1]) % 2 == (new_coords[0]+new_coords[1]) % 2 \
            and abs(own_coords[0]-new_coords[0]) == abs(own_coords[1]-new_coords[1]) \
                or (own_coords[0] == new_coords[0] or own_coords[1] == new_coords[1]):
            return True
        return False


class King(Figure):
    def can_go(self, own_coords: tuple[int, int], new_coords: tuple[int, int]) -> True | False:
        if own_coords[0]-1 <= new_coords[0] <= own_coords[0]+1 \
         and own_coords[1]-1 <= new_coords[1] <= own_coords[1]+1:
            return True
        return False

if __name__ == '__main__':
    p = Pawn()
    print(p)
