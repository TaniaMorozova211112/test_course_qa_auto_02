# Запити до бази даних, які повертають інформацію про студентів,
# зареєстрованих на певний курс, або курси, на які зареєстрований певний студент.

from sqlalchemy.orm import sessionmaker
# імпорт моделей Student, Course і engine
from sqlalchemy_randon_two_table import Student, Course, engine

# Створюємо сесію
Session = sessionmaker(bind=engine)
session = Session()

course_name = "Фізика"

# Знаходимо курс за назвою
course = session.query(Course).filter_by(title=course_name).first()

if course:
    # Виводимо всіх студентів, зареєстрованих на цей курс
    students_in_course = course.students
    print(f"Студенти на курсі '{course_name}':")
    for student in students_in_course:
        print(student.name)
else:
    print(f"Курс '{course_name}' не знайдено")


student_name = "Студент_1"

# Знаходимо студента за ім'ям
student = session.query(Student).filter_by(name=student_name).first()

if student:
    # Виводимо всі курси, на які записаний студент
    courses_of_student = student.courses
    print(f"Курси студента '{student_name}':")
    for course in courses_of_student:
        print(course.title)
else:
    print(f"Студент '{student_name}' не знайдений")


