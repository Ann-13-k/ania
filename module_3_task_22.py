# Задание из Практикума 5.
from math import ceil
class WinDoor:
    """
    Класс, представляющий площадь Окон и Дверей в комнате.
    """
    def __init__(self, x: int | float, y: int | float):
        """
        :param x: int | float: Окна
        :param y: int | float: Двери
        """
        self.square = x * y
class Room:
    """
    Класс "комната" – это класс-контейнер для окон и дверей. Он содержит вызовы класса "окно_дверь"
    """
    def __init__(self, width: int | float, length: int | float, height: int | float):
        """
        Создание и подготовка к работе объекта класса Room "комната".

        :param width: int | float: Ширина комнаты.
        :param length: int | float: Длина комнаты.
        :param height: int | float: Высота комнаты.
        :raise ValueError: Ввели отрицательное число, или которое равно нулю.
        """
        self.width = width
        self.length = length
        self.height = height
        self.wd = []
        if width <= 0 or length <= 0 or height <= 0:
            raise ValueError("Ввели отрицательное число, или которое равно нулю! ")
    @property
    def square(self):
        """
        Декоратор property, внутри которго вычисляем площадь комнаты.

        :return: int | float: Вычисление площади.
        """
        return 2 * self.height * (self.width + self.length)
    def add_wd(self, w: int | float, h: int | float):
        """
        Метод, который добавляет в пустой список значения окон и дверей.

        :param w: int | float: Ширина.
        :param h: int | float: Высота.
        """
        self.wd.append(WinDoor(w, h))
    def work_surface(self) -> float:
        """
        Метод, который рассчитывает обклеиваемую площадь комнаты.
        :return: int | float: Обклеиваемая площадь
        """
        win_door = sum(wd.square for wd in self.wd)
        return self.square - win_door
    def wallpaper_roll(self):
        """
        Метод, который рассчитывает необходимое количество рулонов для обклейки стен.

        :return: int | float: Количество рулонов.
        :raise ValueError: Если ввели отрицательное число, или которое равно нулю.
        """
        width = float(input("Введите ширину рулона обоев: "))
        length = float(input("Введите длину рулона обоев: "))
        if width <= 0 or length <= 0:
            raise ValueError("Ширина или Длина не может быть отрицательным числом, либо равно нулю!")
        return self.work_surface() / (width * length)

print("ЗАДАНИЕ: Программа, которая вычисляет площадь обоев для оклеивания помещения.")
r1 = Room(float(input("Введите ширину комнаты: ")),
          float(input("Введите длинну комнаты: ")),
          float(input("Введите высоту комнаты: ")))
print(f"Площадь стен: {r1.square}")
r1.add_wd(1, 1)
r1.add_wd(1, 1)
r1.add_wd(1, 2)
print(f"Обклеиваемая площадь: {r1.work_surface()}")
print("Теперь рассчитаем необходимое количество рулонов для обклейки стен.")
print(f"Необходимое количество рулонов обоев: {ceil(r1.wallpaper_roll())} шт.")
