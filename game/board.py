import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]

        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y, row in zip(range(self.top, self.top + (self.cell_size * self.height), self.cell_size), self.board):
            for x, pos in zip(range(self.left, self.left + (self.cell_size * self.width), self.cell_size), row):
                # Вначале рисуется цветная клетка, затем белая обводка
                if pos == 1:
                    pygame.draw.ellipse(screen, 'blue',
                                        (x * self.cell_size + self.left,
                                         y * self.cell_size + self.top, self.cell_size,
                                         self.cell_size))
                else:
                    pygame.draw.ellipse(screen, 'red',
                                        (x * self.cell_size + self.left,
                                         y * self.cell_size + self.top, self.cell_size,
                                         self.cell_size))
                pygame.draw.rect(screen, 'white', (x, y, self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        if mouse_pos[1] not in range(self.top, self.top + (self.cell_size * self.height)) or mouse_pos[0] not in range(
                self.left, self.left + (self.cell_size * self.width)):
            return None
        row = (mouse_pos[1] - self.top) // self.cell_size
        column = (mouse_pos[0] - self.left) // self.cell_size
        return (row, column)

    def on_click(self, cell_coords):
        # Смена цвета клетки
        pass

    def get_click(self, mouse_pos):
        cell_coords = self.get_cell(mouse_pos)
        if cell_coords is not None:
            # Реакция на клик по клетке
            self.on_click(cell_coords)