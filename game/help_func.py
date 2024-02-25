import random

import pygame


# Мотивационные фразы, выбор зависит от количества выделенных клеток
# (Чем больше выделенно, тем круче фраза)
motivating_phrases = {
    "common": ["НОРМ", "НАЙС", "КЛАСС", "НЕПЛОХО!", "МОЛОДЕЦ"],
    "uncommon": ["КРУТО", "ОГОО!", "ВАААУ!", "ШОК!", "ВОТ ЭТО ДА"],
    "rare": ["ШОК!!!", "ВОТ ЭТО ДА!!", "КРУТО!!", "ЗДОРОВО!"],
    "silver": ["ТЫ ЛУЧШИЙ!", "НЕУЖЕЛИ??", "НЕВОЗМОЖНО!", "МОЩНО!!"],
    "gold": ["СИЛЬНО!", "ЧТООООО??", "ШИКАРНО!!!"],
    "diamond": ["МОЩНО!!!!", "КАААК???", "ПОТРЯСАЮЩЕ!"],
    "legendary": ["НЕВОЗМОЖНО!!!", "ВЕЛИКОЛЕПНО!!", "ПОТРЯСАЮЩЕ!!!"],
}


# Общая функция вывода текста
def write_text(screen, text, size, color, top, x):
    font = pygame.font.Font("static/fonts/main_font.ttf", size)
    string_rendered = font.render(text, 1, color)
    intro_rect = string_rendered.get_rect()
    intro_rect.top = top
    intro_rect.x = x
    screen.blit(string_rendered, intro_rect)


# Возвращает мотивационную фразу либо фразу об ошибке в виде СПИСКА строк
def get_user_result(result: int):
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


# Печатает мотивационную фразу на экран игрока
def print_user_result(screen, result_text: list):
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


# Печатает очки и количество максимально выделенных клеток игрока за игру
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


# Подсчёт результата выделения
def calculate_the_result(board, score, max_cells, fill_mode=False):
    result_answer = board.result_work()

    if isinstance(result_answer, int):
        score += result_answer * 100
        if result_answer > max_cells:
            max_cells = result_answer

    result_answer = get_user_result(result_answer)

    # В игровом режиме заполнения происходит заполнение поля
    if fill_mode:
        board.generate_board()

    motivation_ticks = pygame.time.get_ticks()

    return {
        "motivation_ticks": motivation_ticks,
        "result_answer": result_answer,
        "score": score,
        "max_cells": max_cells,
    }


# Проверить, нажата ли кнопка возвращения домой
def back_to_lobby_check(coords):
    x, y = coords
    if x in range(2, 54) and y in range(2, 54):
        return True
    return False


# Загрузка звуков происходит только во время запуска игры
def load_sound(pg):
    pg.mixer.pre_init(44100, -16, 1, 512)
    pg.init()

    # Трек на игровой сеанс выбирается случайно
    music = random.choice(
        [
            "daisuke.ogg",
            "miami.ogg",
            "mainmenu.ogg",
            "untitled2.ogg",
            "delay.ogg",
            "release.ogg",
        ]
    )
    pg.mixer.music.load(f"sounds/music/{music}")
    pg.mixer.music.play(-1)
    vol = 0.1
    pg.mixer.music.set_volume(vol)

    # Загрузка всех эмбиентных звуков
    pre_ambient = [
        "click1.wav",
        "click2.wav",
        "click3.wav",
        "collect1.wav",
        "collect2.wav",
        "collect3.wav",
        "collect4.wav",
        "cell.wav",
        "cancel.wav",
        "gohome.wav",
    ]

    # Словарь эмбиентных звуков
    ambient = {
        "click": [],
        "collect": [],
        "cell": [],
        "cancel": [],
        "gohome": [],
    }

    for sound in pre_ambient:
        s = pg.mixer.Sound(f"sounds/ambient/{sound}")
        s.set_volume(0.2)
        for key in ambient.keys():
            if key in sound:
                ambient[key].append(s)
                break

    return [vol, ambient]
