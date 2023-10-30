# --- Imports --- #

from enum import IntEnum, auto


# --- Types Enum --- #

class Types(IntEnum):
    WOOD = auto()
    STICK = auto()
    DIAMOND = auto()


# --- Row Class --- #

class _Row(list):
    def __init__(self, size: int = 3):

        for i in range(size):
            self.append(None)


# --- Matrix Class --- #

class Matrix(list):
    def __init__(self, rows: int = 3, columns: int = 3, recipe = None):

        if recipe != None:
            self = recipe
            return
        
        for i in range(rows):
            self.append(_Row(columns))


# --- Recipe Class --- #

class Recipe(Matrix):
    def __init__(self):
        pass 


# --- CraftingTable Class --- #

class CraftingTable:
    def __init__(self):

        self._table = Matrix()

    def __eq__(self, other):
        return self._table == other

    def add(self, item: Types, row: int, column: int):

        if row >= len(self._table) or row <= -len(self._table):
            return
        if column >= len(self._table[0]) or column <= -len(self._table[0]):
            return

        self._table[row][column] = item

    def remove(self, row: int, column: int):

        if row >= len(self._table) or row <= -len(self._table):
            return
        if column >= len(self._table[0]) or column <= -len(self._table[0]):
            return

        self._table[row][column] = None

    def move(self, row: int, column: int, to_row: int, to_column: int):

        if row >= len(self._table) or row <= -len(self._table):
            return
        if column >= len(self._table[0]) or column <= -len(self._table[0]):
            return

        tmp: Types | None = self._table[row][column]

        self.remove_item(row, column)
        self.add_item(tmp, to_row, to_column)


# --- Testing --- #

if __name__ == "__main__":

    recipe = [[None, Types.DIAMOND, None],
              [None, Types.DIAMOND, None],
              [None, Types.STICK, None]]

    ctable = CraftingTable()

    ctable.add(Types.DIAMOND, 0, 1)
    ctable.add(Types.DIAMOND, 1, 1)
    ctable.add(Types.STICK, 2, 1)
    ctable.add(Types.STICK, 3, 3) #Error, ignore

    print(ctable == recipe)

    ctable.add(Types.WOOD, 2, 0)
    
    print(ctable == recipe)

    
    

        
