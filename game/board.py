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
        color = {
            1: "red_circle.png",
            2: "yellow_circle.png",
            3: "lime_circle.png",
            4: "blue_circle.png",
        }
        for y, row in zip(
            range(
                self.top,
                self.top + (self.cell_size * self.height),
                self.cell_size,
            ),
            self.board,
        ):
            for x, pos in zip(
                range(
                    self.left,
                    self.left + (self.cell_size * self.width),
                    self.cell_size,
                ),
                row,
            ):
                posi = pos
                if posi in range(5, 9):
                    pygame.draw.rect(
                        screen, "gray", (x, y, self.cell_size, self.cell_size)
                    )
                    posi -= 4
                if posi in range(1, 5):
                    circle = pygame.transform.scale(
                        pygame.image.load(
                            f"static/game_sprites/{color[posi]}"
                        ),
                        size=(self.cell_size, self.cell_size),
                    )
                    screen.blit(circle, (x, y))
                if posi == 0:
                    pass
                pygame.draw.rect(
                    screen, "gray", (x, y, self.cell_size, self.cell_size), 1
                )

    def get_cell(self, mouse_pos):
        if (
            mouse_pos[1]
            not in range(self.top, self.top + (self.cell_size * self.height))
        ) or (
            mouse_pos[0]
            not in range(self.left, self.left + (self.cell_size * self.width))
        ):
            return None
        row = (mouse_pos[1] - self.top) // self.cell_size
        column = (mouse_pos[0] - self.left) // self.cell_size
        return (row, column)

    def on_click(self, cell_coords):
        # Смена цвета клетки
        y = cell_coords[0]
        x = cell_coords[1]
        print(y, x, self.board[y][x])
        if self.board[y][x] in range(1, 5):
            self.board[y][x] += 4
        if self.board[y][x] in range(5, 9):
            self.board[y][x] -= 4

    def get_click(self, mouse_pos):
        cell_coords = self.get_cell(mouse_pos)
        if cell_coords is not None:
            # Реакция на клик по клетке
            self.on_click(cell_coords)
