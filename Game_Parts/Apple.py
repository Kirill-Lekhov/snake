from random import randint, choice

from pygame import Color


class Apple:
    COLOR = Color("red")

    def __init__(self):
        self.x, self.y = randint(0, 24), randint(0, 24)

    def get_coord(self) -> tuple:
        return self.x, self.y

    def replace(self, board) -> None:
        all_cells = []

        for row_number, row in enumerate(board):
            for column_number, item in enumerate(row):
                all_cells.append(((column_number, row_number), item[0]))

        empty_cells = list(filter(lambda x: not x[1], all_cells))
        empty_cell = choice(empty_cells)
        self.x, self.y = empty_cell[0]

    def __dict__(self) -> dict:
        return {"color": self.COLOR, "coord": (self.x, self.y)}

    def draw_on_board(self, board, clear_board: bool = True) -> None:
        if clear_board:
            board.clear()

        board[self.x][self.y] = (1, self.COLOR)
