class BaseURL:
    def get_absolute_url(self):
        return f"https://ivashev-edu.com/"
class Course(BaseURL):
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
    def get_absolute_url(self):
        base_url = super().get_absolute_url()
        return f"{base_url}/courses/{self.title}"
class StudentProfile(BaseURL):
    def __init__(self, full_name, email):
        self.full_name = full_name
        self.email = email
    def get_absolute_url(self):
        base_url = super().get_absolute_url()
        return f"{base_url}/profiles/{self.full_name}"

a = Course("635165", "1515")
print(a.get_absolute_url())
b = StudentProfile("541654", "555")
print(b.get_absolute_url())