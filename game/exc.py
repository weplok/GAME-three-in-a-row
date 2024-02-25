# Когда выделено меньше 3 клеток
class LessThanThreeError(Exception):
    pass


# Когда выделены клетки разных цветов
class OnlyOneColorError(Exception):
    pass


# Когда выделена пустая клетка
class BlackCellError(Exception):
    pass


# Исключение для обработки возвращения в меню
class BackToMenu(Exception):
    pass
