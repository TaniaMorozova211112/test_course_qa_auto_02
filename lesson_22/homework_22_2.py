# Виконання базових операцій: додаємо нового студента до бази даних
# та додаємо його до певного курсу. Перевіряємо, що ці зміни коректно
# відображаються у базі даних.

from sqlalchemy.orm import sessionmaker
# імпорт моделей Student, Course і engine
from sqlalchemy_randon_two_table import Student, Course, engine
from sqlalchemy import func


# Створюємо сесію
Session = sessionmaker(bind=engine)
session = Session()

# Вводимо ім'я нового студента
new_student_name = input("\nВведіть прізвище та ім'я нового студента: ").strip()


# Перевірка чи студент вже існує
existing_student = session.query(Student).filter_by(name=new_student_name).first()
if existing_student:
    print(f"\nСтудент з ім'ям '{new_student_name}' уже існує.")
else:
    # Отримуємо всі курси з бази даних
    courses = session.query(Course).all()

    # Виводимо список доступних курсів
    print("\nДоступні курси:")
    for course in courses:
        print(f"- {course.title}")

    # Змінна для збереження обраного курсу
    chosen_course = None

    # Поки не вибрано дійсний курс, повторюємо запит
    while not chosen_course:
        # Запит назви курсу від користувача
        chosen_course_title = input("\nВведіть назву курсу для запису студента: ").strip()

        # Шукаємо курс у списку курсів, порівнюючи назви без урахування регістру
        for course in courses:
            if course.title.lower() == chosen_course_title.lower():
                chosen_course = course
                break  # Вийти з циклу, якщо курс знайдено

        # Якщо курс не знайдено, виводимо повідомлення і запит повторюємо
        if not chosen_course:
            print(f"\nКурс '{chosen_course_title}' не знайдено. Спробуйте ще раз.")

    # Додаємо нового студента та прив'язуємо його до обраного курсу
    new_student = Student(name=new_student_name)
    new_student.courses.append(chosen_course)

    # Додаємо студента в сесію та зберігаємо у базі
    session.add(new_student)
    session.commit()

    print(f"\nСтудент '{new_student_name}' "
          f"успішно доданий на курс '{chosen_course.title}'.")

# Після commit перевіряємо, що наші зміни коректно
# відображаються у базі даних.
print("\nВсі студенти та їх курси після додавання нового:")

all_students = session.query(Student).all()
for student in all_students:
    course_titles = [course.title for course in student.courses]
    print(f"{student.name} навчається на курсах: {course_titles}")


