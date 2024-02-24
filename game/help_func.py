import random

import pygame


motivating_phrases = {
    "common": ["НОРМ", "НАЙС", "КЛАСС", "НЕПЛОХО!", "МОЛОДЕЦ"],
    "uncommon": ["КРУТО", "ОГОО!", "ВАААУ!", "ШОК!", "ВОТ ЭТО ДА"],
    "rare": ["ШОК!!!", "ВОТ ЭТО ДА!!", "КРУТО!!", "ЗДОРОВО!"],
    "silver": ["ТЫ ЛУЧШИЙ!", "НЕУЖЕЛИ??", "НЕВОЗМОЖНО!", "МОЩНО!!"],
    "gold": ["СИЛЬНО!", "ЧТООООО??", "ШИКАРНО!!!"],
    "diamond": ["МОЩНО!!!!", "КАААК???", "ПОТРЯСАЮЩЕ!"],
    "legendary": ["НЕВОЗМОЖНО!!!", "ВЕЛИКОЛЕПНО!!", "ПОТРЯСАЮЩЕ!!!"],
}


def get_user_result(result):
    if result == "ONLY ONE COLOR":
        result_text = ["ТОЛЬКО", "ОДИН ЦВЕТ"]
    elif result == "LESS THAN THREE":
        result_text = ["БОЛЬШЕ", "ТРЁХ КЛЕТОК"]
    elif result == "NO BLACK CELLS":
        result_text = ["НЕ ТРОГАЙ", "ПУСТЫЕ КЛЕТКИ"]
    elif result in range(3, 5):
        result_text = [random.choice(motivating_phrases["common"])]
    elif result in range(5, 8):
        result_text = [random.choice(motivating_phrases["uncommon"])]
    elif result in range(8, 11):
        result_text = [random.choice(motivating_phrases["rare"])]
    elif result in range(11, 15):
        result_text = [random.choice(motivating_phrases["silver"])]
    elif result in range(15, 20):
        result_text = [random.choice(motivating_phrases["gold"])]
    elif result in range(20, 27):
        result_text = [random.choice(motivating_phrases["diamond"])]
    else:
        result_text = [random.choice(motivating_phrases["legendary"])]
    return result_text


def print_user_result(screen, result_text):
    if result_text == 0:
        result_text = []
    font = pygame.font.Font("static/fonts/pixel_font.ttf", 108)

    top = 100
    for text in reversed(result_text):
        string_rendered = font.render(text, 1, "#FF50B0")
        intro_rect = string_rendered.get_rect()
        intro_rect.top = top
        intro_rect.x = 300 - intro_rect.width / 2
        top -= 90
        screen.blit(string_rendered, intro_rect)


def print_user_score(screen, score, max_cells):
    font = pygame.font.Font("static/fonts/pixel_font.ttf", 40)

    score_rendered = font.render(
        f"Счёт: {str(score)}",
        1,
        "#E8CED7",
    )
    score_rect = score_rendered.get_rect()
    score_rect.top = 965
    score_rect.x = 20
    screen.blit(score_rendered, score_rect)

    max_cells_rendered = font.render(
        f"Максимум клеток: {str(max_cells)}",
        1,
        "#E8CED7",
    )
    max_cells_rect = max_cells_rendered.get_rect()
    max_cells_rect.top = 965
    max_cells_rect.x = 580 - max_cells_rect.width
    screen.blit(max_cells_rendered, max_cells_rect)
