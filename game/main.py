import pygame

from game_board import Three


def main():
    pygame.init()
    size = 600, 1000
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Три в ряд')

    board = Three(16, 22, screen)
    board.set_view(20, 200, 35)

    board.render(screen)

    pygame.display.flip()

    mouse_down_flag = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                cell = board.get_cell(event.pos)
                if cell is not None:
                    mouse_down_flag = True
                    board.get_clicked_pos(cell[1], cell[0])

            if event.type == pygame.MOUSEMOTION and mouse_down_flag:
                if board.get_cell(event.pos) is None:
                    mouse_down_flag = False
                    break
                cell = board.get_cell(event.pos)
                board.get_clicked_pos(cell[1], cell[0])

            if event.type == pygame.MOUSEBUTTONUP and mouse_down_flag:
                mouse_down_flag = False
                print(board.result_work())

            screen.fill((0, 0, 0))
            board.render(screen)
            pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
