# Задача 1:
class Person:
    name = ''
    parent = None

grandmother = Person()
grandmother.name = 'Бабушка'

mother = Person()
mother.name = 'Мама'
mother.parent = grandmother.name

daughter = Person()
daughter.name = 'Дочка'
daughter.parent = mother.name

print(daughter.name)
print(daughter.parent)
daughter.parent = grandmother.name
print(daughter.parent)

# Задача 2:
class LogRow:
    def __init__(self, row_id, client, item, amount):
        self.row_id = row_id
        self.client = client
        self.item = item
        self.amount = amount
    def __str__(self):
        return f'Порядковый номер: {self.row_id}'

class LogManager:
    def __init__(self, objects=None):
        self.objects = objects if objects else []
    def objects_count(self):
        return len(self.objects)
    def total_amount(self):
        return sum(row.amount for row in self.objects)

row1 = LogRow(1, 'Иванов Иван', 'iPhone', 1000)
row2 = LogRow(2, 'Иванова Мария', 'Бритва gillette fusion', 100)
row3 = LogRow(3, 'Петрова Ольга', 'Билет на Мальдивы', 3990)

log = LogManager([row1, row2, row3])

print(row1, row2, row3)
print(f'Всего объектов в логе: {log.objects_count()}')
print(f'Общая сумма всех покупок: {log.total_amount()}')