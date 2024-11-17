class Course:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
    def __str__(self):
        return (f"Название курса: {self.title}"
                f"\nПродолжительность обучения - {self.duration}.")
    def get_absolute_url(self):
        return f"Ссылка на курс: https://ivashev-edu.com/courses/{self.title}"

class StudentProfile:
    def __init__(self, full_name, email):
        self.full_name = full_name
        self.email = email
    def __str__(self):
        return (f"Имя пользователя: {self.full_name} "
                f"\nЭлектронный адрес: {self.email}")
    def get_absolute_url(self):
        return f"Ссылка на профиль: https://ivashev-edu.com/profiles/{self.email.replace('@mail.ru', '')}"

course = Course("Python-Basics", "21 неделя")
course1 = Course("Telegram-Bots", "8 недель")
print(course, '\n', course.get_absolute_url())
print(course1, '\n', course1.get_absolute_url())

student_profile = StudentProfile("John Snow", "john@mail.ru")
student_profile1 = StudentProfile("Daenerys Targaryen", "daene3@mail.ru")
print(student_profile, '\n', student_profile.get_absolute_url())
print(student_profile1, "\n", student_profile1.get_absolute_url())