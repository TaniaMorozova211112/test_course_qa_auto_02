# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючий студента.
# Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.

# створюємо клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
class Student:
    def __init__(self, first_name, last_name, age, average_score):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_score = average_score

# налаштовуємо перетворення у рядкове представлення для виводу
    def __str__(self):
        return (
               f"Студент {self.first_name} {self.last_name}."
               f" Вік - {self.age}, середній бал - {self.average_score}."
        )

# додаємо метод до класу "Студент", який дозволяє змінювати середній бал студента.
    def change_average_score(self, new_average_score):
        old_score = self.average_score
        self.average_score = new_average_score
        return (
               f"Попередній середній бал студента: {old_score}.\n"
               f"Новий середній бал студента: {new_average_score}."
        )


# створюємо об'єкт цього класу, представляючий студента.
student_01 = Student(
    "Tetiana",
    "Morozova",
         41,
 98
)

# виводимо інформацію про студента та змінюємо його середній бал.
print(student_01)   # початкова інформація

print(student_01.change_average_score(100))   # зміна бала

print(student_01)   # перевірка нового бала




