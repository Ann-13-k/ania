# Задание №1:
class Publication:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return (f"Название публикации: {self.title}\n"
                f"Автор публикации: {self.author}\n"
                f"Год издания публикации: {self.year}")
class Book(Publication):
    def __init__(self, genre, title, author, year):
        super().__init__(title, author, year)
        self.genre = genre
    def get_info(self):
        public = super().get_info()
        return (f"{public}\n"
                f"Жанр книги: {self.genre}")
class Magazine(Publication):
    def __init__(self, issue_number, title, author, year):
        super().__init__(title, author, year)
        self.issue_number = issue_number
    def get_info(self):
        public = super().get_info()
        return (f"{public}\n"
                f"Номер выпуска журнала: {self.issue_number}")
class Newspaper(Publication):
    def __init__(self, publisher, title, author, year):
        super().__init__(title, author, year)
        self.publisher = publisher
    def get_info(self):
        public = super().get_info()
        return (f"{public}\n"
                f"Издатель газеты: {self.publisher}")

print("ЗАДАНИЕ №1. СИСТЕМА ДЛЯ УПРАВЛЕНИЯ БИБЛИОТЕКОЙ \n")
book = Book("Фантастика и фэнтези, Триллер", "Игра престолов", "Мартин Джордж Рэймонд Ричард", "1996 год")
book2 = Book("Ужасы", "В полумраке ужаса", "Стивен Кинг", "2017 год")
print(f"КНИГА №1:\n{book.get_info()}\n")
print(f"КНИГА №2:\n{book2.get_info()}\n")

magazine = Magazine("№3", "Тело в моде, искусстве, активизме", "VOGUE", "март 2022 года")
magazine2 = Magazine("№3", "Журналист", "ООО «Медиагруппа „Журналист“»", "2024 год")
print(f"ЖУРНАЛ №1:\n{magazine.get_info()}\n")
print(f"ЖУРНАЛ №2:\n{magazine2.get_info()}\n")

newspaper = Newspaper('ООО "ДЕФИ"', "THE ART NEWSPAPER RUSSIA", "Ольга Ярутина", "07 сентября 2024")
newspaper2 = Newspaper('АО "Спорт-Экспресс"', "СПОРТ-ЭКСПРЕСС", "Владимир Кучмий", "15 октября 2024")
print(f"ГАЗЕТА №1:\n{newspaper.get_info()}\n")
print(f"ГАЗЕТА №2:\n{newspaper2.get_info()}\n")

# Задание №2:
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_info(self):
        return (f"Название продукта: {self.name}\n"
                f"Цена продукта: {self.price}")
class Product(Item):
    def __init__(self, name, price, brand, category):
        super().__init__(name, price)
        self.brand = brand
        self.category = category
    def get_brand(self):
        return f"Бренд продукта: {self.brand}"
    def get_info(self):
        item = super().get_info()
        return (f"{item}\n"
                f"Категория продукта: {self.category}")
class Food(Product):
    def __init__(self, name, price, brand, category, expire_date, weight):
        super().__init__(name, price, brand, category)
        self.expire_date = expire_date
        self.weight = weight
    def get_expiry_date(self):
        return f"Срок годности продукта: {self.expire_date}"
    def get_info(self):
        item = super().get_info()
        return (f"{item}\n"
                f"Вес продукта: {self.weight}")
class Beverage(Product):
    def __init__(self, name, price, brand, category, volume, carbonated):
        super().__init__(name, price, brand, category)
        self.volume = volume
        self.carbonated = carbonated
    def is_carbonated(self):
        return f"Флаг указывающий, является ли напиток газированным: {self.carbonated}"
    def get_info(self):
        item = super().get_info()
        return (f"{item}\n"
                f"Объем напитка в миллилитрах: {self.volume}")


print("ЗАДАНИЕ №2. СИСТЕМА ДЛЯ УЧЕТА ПРОДУКТОВ \n")
food1 = Food("Banana", 1.99, "Chiquita", "Fruit", "2023-01-31", 150)
print(food1.get_info())
print(food1.get_brand())
print(food1.get_expiry_date(), "\n")

food2 = Food("Cheese", 4.99, "Kraft", "Dairy", "2022-12-15", 250)
print(food2.get_info())
print(food2.get_brand())
print(food2.get_expiry_date(), "\n")

beverage1 = Beverage("Coca Cola", 2.49, "Coca Cola Company", "Soft Drink", 500, True)
print(beverage1.get_info())
print(beverage1.get_brand())
print(beverage1.is_carbonated(), "\n")

beverage2 = Beverage("Water", 0.99, "Aquafina", "Bottled Water", 1000, False)
print(beverage2.get_info())
print(beverage2.get_brand())
print(beverage2.is_carbonated())
