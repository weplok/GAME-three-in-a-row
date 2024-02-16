import pygame

from game_board import Lines


def main():
    pygame.init()
    size = 600, 1000
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption('Линеечки')

    board = Lines(16, 22)
    board.set_view(20, 200, 35)

    ticks = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)

        screen.fill((0, 0, 0))
        board.render(screen)
        if ticks == 50:
            ticks = 0
        pygame.display.flip()
        clock.tick(50)
        ticks += 1
    pygame.quit()


if __name__ == '__main__':
    main()
