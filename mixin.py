class BoardValidationMixin:
    __list_letters = ["A", "B", "C", "D", "E", "F", "G", "H"]

    def validator(self, coords: str) -> True | False:
        try:
            element_1, element_2 = coords
            print(element_1, element_2)
            if len(element_1) > 1 or len(element_2) > 1:
                return False
            if element_1.isdigit():
                return False
            if element_2.isalpha():
                return False
            if element_1.upper() not in self.__list_letters:
                return False
            if not (1 <= int(element_2) <= 8):
                return False
            return True
        except ValueError:
            return False

    def convert_coords(self, coords: str) -> tuple[int, int] | None:
        if self.validator(coords):
            element1, element_2 = coords
            coord_1 = self.__list_letters.index(element1.upper())
            coord_2 = int(element_2) - 1
            return (coord_1, coord_2)
        else:
            return None
