import pygame

from board import Board


class Lines(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.selected_cell = None

    def has_path(self, x1, y1, x2, y2):
        # словарь расстояний
        d = {(x1, y1): 0}
        v = [(x1, y1)]
        while len(v) > 0:
            x, y = v.pop(0)
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if dx * dy != 0:
                        continue
                    if x + dx < 0 or x + dx >= self.width or y + dy < 0 or y + dy >= self.height:
                        continue
                    if self.board[y + dy][x + dx] == 0:
                        dn = d.get((x + dx, y + dy), -1)
                        if dn == -1:
                            d[(x + dx, y + dy)] = d.get((x, y), -1) + 1
                            v.append((x + dx, y + dy))
        dist = d.get((x2, y2), -1)
        return dist >= 0

    def on_click(self, cell):

        y = cell[0]
        x = cell[1]
        if self.selected_cell is None:

            if self.board[y][x] == 1:
                self.selected_cell = x, y
            else:
                self.board[y][x] = 1

        else:
            if self.selected_cell == (x, y):
                self.selected_cell = None
                return

            x2 = self.selected_cell[0]
            y2 = self.selected_cell[1]
            if self.has_path(x2, y2, x, y):
                self.board[y][x] = 1
                self.board[y2][x2] = 0
                self.selected_cell = None

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):

                if self.board[y][x] == 1:
                    color = pygame.Color("blue")
                    if self.selected_cell == (x, y):
                        color = pygame.Color("red")
                    pygame.draw.ellipse(screen, color,
                                        (x * self.cell_size + self.left,
                                         y * self.cell_size + self.top, self.cell_size,
                                         self.cell_size))

                pygame.draw.rect(screen, pygame.Color(255, 255, 255),
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                  self.cell_size,
                                  self.cell_size), 1)
