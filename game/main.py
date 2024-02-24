import sys

from game_board import Three

from help_func import (
    BackToMenu,
    back_to_lobby_check,
    calculate_the_result,
    print_user_result,
    print_user_score,
    write_text,
)

import pygame


def start_menu(render_score):
    global score, max_cells

    intro_text = [
        "ТРИ В РЯД! ПРОТОТИП",
        "ИГРАТЬ",
        "Режим игры:",
        "С заполнением",
        "Без заполнения",
    ]
    color = pygame.Color("pink")

    # Загрузка фона меню
    fon = pygame.transform.scale(
        pygame.image.load("static/game_backgrounds/fon.jpg"),
        (size[0], size[1]),
    )
    screen.blit(fon, (0, 0))

    # Основное меню
    write_text(screen, intro_text[0], 65, color, 80, 40)
    write_text(screen, intro_text[1], 50, color, 400, 230)
    pygame.draw.rect(screen, "white", (220, 395, 160, 60), 2)
    if render_score:
        write_text(screen, f"Счёт: {score}", 65, color, 700, 40)
        write_text(screen, f"Максимум клеток: {max_cells}", 65, color, 800, 40)

    main_menu = True
    while main_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(220, 380) and event.pos[1] in range(
                    395, 455
                ):
                    main_menu = False
        pygame.display.flip()

    # Меню выбора режима игры
    fon = pygame.transform.scale(
        pygame.image.load("static/game_backgrounds/fon.jpg"),
        (size[0], size[1]),
    )
    screen.blit(fon, (0, 0))
    write_text(screen, intro_text[0], 65, color, 80, 40)
    write_text(screen, intro_text[2], 50, color, 400, 180)
    write_text(screen, intro_text[3], 50, color, 500, 50)
    pygame.draw.rect(screen, "white", (45, 495, 320, 55), 2)
    write_text(screen, intro_text[4], 50, color, 570, 50)
    pygame.draw.rect(screen, "white", (45, 565, 320, 55), 2)
    if render_score:
        write_text(screen, f"Счёт: {score}", 65, color, 700, 40)
        write_text(screen, f"Максимум клеток: {max_cells}", 65, color, 800, 40)

    choose_game_mode = True
    global FILL_MODE
    while choose_game_mode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(45, 365) and event.pos[1] in range(
                    495, 550
                ):
                    FILL_MODE = True
                    choose_game_mode = False
                if event.pos[0] in range(45, 365) and event.pos[1] in range(
                    565, 620
                ):
                    FILL_MODE = False
                    choose_game_mode = False
        pygame.display.flip()

    # Выход из меню
    return


def game_proccess():
    global motivation_ticks, result_answer
    global score, max_cells

    board = Three(16, 21, screen)
    board.set_view(20, 235, 35)

    board.render(screen)

    pygame.display.flip()

    mouse_down_flag = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    cell = board.get_cell(event.pos)
                    if cell is not None:
                        mouse_down_flag = True
                        board.get_clicked_pos(cell[1], cell[0])
                    elif back_to_lobby_check(event.pos):
                        raise BackToMenu()
                elif event.button == 3:
                    mouse_down_flag = False
                    board.cancel_the_selection()

            if event.type == pygame.MOUSEMOTION and mouse_down_flag:
                if board.get_cell(event.pos) is None:
                    mouse_down_flag = False
                    board.cancel_the_selection()
                    break
                cell = board.get_cell(event.pos)
                board.get_clicked_pos(cell[1], cell[0])

            if event.type == pygame.MOUSEBUTTONUP and mouse_down_flag:
                if event.button == 1:
                    mouse_down_flag = False
                    result = calculate_the_result(
                        board, score, max_cells, FILL_MODE
                    )
                    result_answer = result["result_answer"]
                    score = result["score"]
                    max_cells = result["max_cells"]
                    motivation_ticks = result["motivation_ticks"]

        if motivation_ticks != -1:
            seconds = (pygame.time.get_ticks() - motivation_ticks) / 1000
            if seconds > 2:
                motivation_ticks = -1
                result_answer = 0

        screen.fill((0, 0, 0))

        fon = pygame.transform.scale(
            pygame.image.load("static/game_backgrounds/game_fon.jpg"),
            (size[0], size[1]),
        )
        screen.blit(fon, (0, 0))

        board.render(screen)
        print_user_result(screen, result_answer)
        print_user_score(screen, score, max_cells)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    pygame.init()
    size = 600, 1000
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Три в ряд. ПРОТОТИП")

    render_score_flag = False
    FILL_MODE = False
    while True:
        start_menu(render_score_flag)
        try:
            score, max_cells = 0, 0
            result_answer = 0
            motivation_ticks = -1
            game_proccess()
        except BackToMenu:
            render_score_flag = True
