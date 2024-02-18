import pygame

from random import randint

from board import Board
import exc


class Three(Board):
    def __init__(self, width, height, screen):
        super().__init__(width, height)
        self.screen = screen
        self.generate_board()
        self.pressed_pos_list = list()

    def generate_board(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 0:
                    self.board[y][x] = randint(1, 4)

    def get_clicked_pos(self, x, y):
        if [x, y] not in self.pressed_pos_list:
            self.pressed_pos_list.append([x, y])
            if self.board[y][x] != 0:
                self.board[y][x] += 4

    def worked_pressed_pos(self):  # В будущем отлавливавать Exception, а не return

        first_x = self.pressed_pos_list[0][0]
        first_y = self.pressed_pos_list[0][1]
        main_color = self.board[first_y][first_x]
        self.board[first_y][first_x] -= 4

        success_count = 1
        one_color = True

        for x, y in self.pressed_pos_list[1:]:
            if self.board[y][x] == main_color:
                success_count += 1
            else:
                one_color = False
            self.board[y][x] -= 4
        if len(self.pressed_pos_list) < 3:
            raise exc.LessThanThreeError
        if one_color:
            return success_count
        raise exc.OnlyOneColorError

    def result_work(self):
        try:
            answer = self.worked_pressed_pos()
        except exc.OnlyOneColorError:
            answer = "ONLY ONE COLOR"
        except exc.LessThanThreeError:
            answer = "LESS THAN THREE"
        else:
            for x, y in self.pressed_pos_list:
                self.board[y][x] = 0
        self.pressed_pos_list = list()

        return answer
