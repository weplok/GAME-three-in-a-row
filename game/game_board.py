from random import choice, randint

from board import Board

import exc


class Three(Board):
    def __init__(self, width, height, screen, ambient):
        super().__init__(width, height)
        self.screen = screen

        # Словарь эмбиентных звуков, создается в help_func.load_sound()
        self.ambient = ambient

        self.generate_board()

        # Нажатые клетки
        self.pressed_pos_list = list()

        # Рекорды текущей игры
        self.records = {"score": 0, "max_cells": 0}

    # Случайная генерация цветных клеток
    def generate_board(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 0:
                    self.board[y][x] = randint(1, 4)

    # Отмена выделения клеток
    def cancel_the_selection(self):
        try:
            self.worked_pressed_pos()
        except Exception:
            pass
        choice(self.ambient["cancel"]).play()
        self.pressed_pos_list = list()

    # Добавление клетки в список нажатых (если ещё не нажата)
    def get_clicked_pos(self, x, y):
        if [x, y] not in self.pressed_pos_list:
            self.pressed_pos_list.append([x, y])
            if self.board[y][x] != 0:
                self.board[y][x] += 4
                choice(self.ambient["cell"]).play()

    # "Зажимание" клеток, подсчёт количества успешно
    # выделенных клеток или возврат исключения
    def worked_pressed_pos(self):
        # Обработка первой нажатой клетки.
        # Цвета следующих нажатых клеток будут сравниваться с цветом первой
        first_x = self.pressed_pos_list[0][0]
        first_y = self.pressed_pos_list[0][1]
        main_color = self.board[first_y][first_x]
        if self.board[first_y][first_x] != 0:
            self.board[first_y][first_x] -= 4
            black_cell = False
        else:
            black_cell = True

        one_color = True
        success_count = 1
        # Обработка следующих клеток
        for x, y in self.pressed_pos_list[1:]:
            if self.board[y][x] == main_color:
                success_count += 1
            else:
                one_color = False
            if self.board[y][x] != 0:
                self.board[y][x] -= 4

        # Обработка исключений (описания см. в exc.py)
        if black_cell:
            raise exc.BlackCellError
        if len(self.pressed_pos_list) < 3:
            raise exc.LessThanThreeError
        if one_color:
            return success_count
        raise exc.OnlyOneColorError

    # Возвращает результат работы (из worked_pressed_pos())
    def result_work(self):
        try:
            answer = self.worked_pressed_pos()
        except exc.OnlyOneColorError:
            answer = "ONLY ONE COLOR"
            choice(self.ambient["cancel"]).play()
        except exc.LessThanThreeError:
            answer = "LESS THAN THREE"
            choice(self.ambient["cancel"]).play()
        except exc.BlackCellError:
            answer = "NO BLACK CELLS"
            choice(self.ambient["cancel"]).play()
        else:
            choice(self.ambient["collect"]).play()
            for x, y in self.pressed_pos_list:
                # Символом А помечаются успешно выделенные клетки
                self.board[y][x] = "A"
            self.after_success_work()
        self.pressed_pos_list = list()
        return answer

    # "Падение" клеток вниз после исчезновения выделенных
    def after_success_work(self):
        # Для удобной работы поле клеток транспонируется
        board_trans = [list(tup) for tup in zip(*self.board)]

        # Само "падение"
        edited_rows = list()
        for row in range(len(board_trans)):
            if "A" in board_trans[row]:
                new_row = board_trans[row][:]
                while "A" in new_row:
                    new_row.remove("A")
                new_row = "".join(list(map(str, new_row)))
                new_row = new_row.rjust(len(board_trans[row]), "0")
                new_row = list(map(int, new_row))
                edited_rows.append([row, new_row])
        for row in edited_rows:
            board_trans[row[0]] = row[1]

        # Обработанное поле транспонируется обратно
        self.board = [list(tup) for tup in zip(*board_trans)]
