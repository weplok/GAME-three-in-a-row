import pygame


def print_user_result(screen, result):
    if result == 0:
        result_text = []
        return
    elif result == "ONLY ONE COLOR":
        result_text = ["ТОЛЬКО", "ОДИН ЦВЕТ"]
    elif result == "LESS THAN THREE":
        result_text = ["БОЛЬШЕ ТРЁХ", "КЛЕТОК"]
    elif result == "NO BLACK CELLS":
        result_text = ["НЕ ТРОГАЙ", "ЧЁРНЫЕ КЛЕТКИ"]
    elif result > 16:
        result_text = ["НЕВОЗМОЖНО!!"]
    else:
        result_text = [motivating_phrases[result]]
    font = pygame.font.Font("static/main_font.ttf", 90)

    top = 10
    for text in result_text:
        string_rendered = font.render(text, 1, "green")
        intro_rect = string_rendered.get_rect()
        intro_rect.top = top
        intro_rect.x = 300 - intro_rect.width / 2
        top += 90
        screen.blit(string_rendered, intro_rect)


motivating_phrases = {
    3: "НОРМ",
    4: "НАЙС",
    5: "КЛАСС",
    6: "КРУТО",
    7: "ОГОО!",
    8: "ВАААУ!!",
    9: "ШОК!",
    10: "ВОТ ЭТО ДА",
    11: "КРУТО!!",
    12: "СИЛЬНО!",
    13: "МОЩНО!!",
    14: "ТЫ ЛУЧШИЙ!",
    15: "НЕУЖЕЛИ??",
    16: "КАААК???",
}
