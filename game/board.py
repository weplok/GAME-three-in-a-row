import pygame


class Board:
    def __init__(self, width, height):
        # Количество клеток поля в длину и ширину
        self.width = width
        self.height = height

        # ПОЛЕ. Храниться в виде списка списков
        self.board = [[0] * width for _ in range(height)]

        # Координаты левой верхней клетки и размер всех клеток
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # Изменение координат левой верхней клетки и размера всех клеток
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    # Отрисовка игрового поля
    def render(self, screen):
        sprites = {
            1: "red_circle.png",
            2: "yellow_circle.png",
            3: "lime_circle.png",
            4: "blue_circle.png",
        }

        # Проходимся циклами по self.board для его отрисовки
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
                # Для удобства значение клетки дублируется в переменную posi
                posi = pos

                # Если клетка выделена
                if posi in range(5, 9):
                    pygame.draw.rect(
                        screen, "gray", (x, y, self.cell_size, self.cell_size)
                    )
                    posi -= 4

                # Отрисовка заполненных клеток
                if posi in range(1, 5):
                    circle = pygame.transform.scale(
                        pygame.image.load(
                            f"static/game_sprites/{sprites[posi]}"
                        ),
                        size=(self.cell_size, self.cell_size),
                    )
                    screen.blit(circle, (x, y))

                # Отрисовка пустых клеток
                if posi == 0:
                    pass

                # Отрисовка самой клетки
                pygame.draw.rect(
                    screen, "gray", (x, y, self.cell_size, self.cell_size), 1
                )

    # Получить координаты клетки в self.board по координатам нажатия мышки
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
