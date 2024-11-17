from dataclasses import dataclass
@dataclass
class Student:
    name: str
    age: int
    major: str
    gpa: float
    def display_info(self):
        print(f"Имя студента: {self.name}\n"
              f"Возвраст студента: {self.age}\n"
              f"Специальность: {self.major}\n"
              f"Средний балл студента: {self.gpa}\n")
    def calculate_grade(self):
        if self.gpa < 3:
            return "Неудовлетворительно"
        elif self.gpa < 4:
            return "Удовлетворительно"
        elif self.gpa < 5:
            return "Хорошо"
        else:
            return "Отлично"

    def __str__(self):
        return f"{self.name} - средний бал: {self.gpa}"
def sorting_students(students):
    return sorted(students, key=lambda student: student.gpa, reverse=True)

# Создание списка студентов
students = [
    Student("Alice", 20, "Computer Science", 3.8),
    Student("Bob", 22, "Engineering", 3.2),
    Student("Charlie", 21, "Mathematics", 4.5),
    Student("David", 23, "Physics", 2.7),
    Student("Eve", 19, "Biology", 3.9)]

# Отображение информации о студентах
for student in students:
    student.display_info()

# Сравнение студентов
print("Are Alice and Bob the same student?", students[0] == students[1])
print("Are Alice and Eve the same student?", students[0] == students[4], "\n")

# Расчет и вывод оценок
for student in students:
    print(f"{student.name} - Grade: {student.calculate_grade()}")

# Сортировка студентов по среднему баллу
sorting = sorting_students(students)
print("\nСортированные студенты по среднему баллу: ")
for student in sorting:
    print(student)