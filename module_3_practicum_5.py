from math import ceil
class WinDoor:
    def __init__(self, x, y):
        self.square = x * y
class Room:
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height
        self.wd = []
    @property
    def square(self):
        return 2 * self.height * (self.width + self.length)
    def add_wd(self, w, h):
        self.wd.append(WinDoor(w, h))
    def work_surface(self):
        win_door = sum(wd.square for wd in self.wd)
        return self.square - win_door
    def wallpaper_roll(self):
        width = float(input("Введите ширину рулона обоев: "))
        length = float(input("Введите длину рулона обоев: "))
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

