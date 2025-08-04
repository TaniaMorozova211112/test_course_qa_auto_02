# Оновлення даних про студентів або курси,
# а також видалення студентів з бази даних.

# Імпортуємо необхідні класи з SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy_randon_two_table import Student, Course, engine

# Створення сесії для взаємодії з базою даних
Session = sessionmaker(bind=engine)
session = Session()

# Функція для виведення всіх студентів і курсів, на яких вони навчаються
def print_all_students_courses():
    print("\nАктуальні дані в базі студентів та курсів:")
    all_students = session.query(Student).all()
    for student in all_students:
        course_titles = [course.title for course in student.courses]
        print(f"{student.name} навчається на курсах: {course_titles}")

# Функція пошуку студента без врахування регістру
def find_student_by_name_case_insensitive(name):
    name_lower = name.lower()
    all_students = session.query(Student).all()
    for student in all_students:
        if student.name.lower() == name_lower:
            return student
    return None  # Якщо студент не знайдений

# Функція пошуку курсу без врахування регістру
def find_course_by_title_case_insensitive(title):
    title_lower = title.lower()
    all_courses = session.query(Course).all()
    for course in all_courses:
        if course.title.lower() == title_lower:
            return course
    return None  # Якщо курс не знайдений

# Функція оновлення імені студента
def update_student_name():
    print("\nСписок усіх студентів:")
    all_students = session.query(Student).all()
    for student in all_students:
        print(f"- {student.name}")

    # Отримуємо старе ім’я і шукаємо студента в базі
    old_name = input("\nВведіть старе ім'я студента для оновлення: ").strip()
    student = find_student_by_name_case_insensitive(old_name)

    if not student:
        print(f"\nСтудент з ім'ям '{old_name}' не знайдений.")
        return

    # Отримуємо нове ім’я та приводимо до формату: кожне слово з великої літери
    new_name_raw = input("\nВведіть нове ім'я студента: ").strip()
    new_name = new_name_raw.title()
    student.name = new_name
    session.commit()  # Зберігаємо зміни
    print(f"\nІм'я студента '{old_name}' оновлено на '{new_name}'.")

# Функція оновлення назви курсу
def update_course_title():
    print("\nСписок усіх курсів:")
    all_courses = session.query(Course).all()
    for course in all_courses:
        print(f"- {course.title}")

    # Отримуємо стару назву і шукаємо курс
    old_title = input("\nВведіть стару назву курсу для оновлення: ").strip()
    course = find_course_by_title_case_insensitive(old_title)

    if not course:
        print(f"\nКурс з назвою '{old_title}' не знайдений.")
        return

    # Отримуємо нову назву курсу і форматуємо її
    new_title_raw = input("\nВведіть нову назву курсу: ").strip()
    new_title = new_title_raw.title()
    course.title = new_title
    session.commit()  # Зберігаємо зміни
    print(f"\nНазва курсу '{old_title}' оновлена на '{new_title}'.")

# Функція для видалення студента з бази
def delete_student():
    print("\nСписок усіх студентів:")
    all_students = session.query(Student).all()
    for student in all_students:
        print(f"- {student.name}")

    # Отримуємо ім’я для видалення
    del_name = input("\nВведіть ім'я студента, якого потрібно видалити: ").strip()
    student = find_student_by_name_case_insensitive(del_name)

    if not student:
        print(f"\nСтудент з ім'ям '{del_name}' не знайдений.")
        return

    session.delete(student)
    session.commit()  # Застосовуємо видалення
    print(f"\nСтудент '{del_name}' видалений з бази даних.")

# Основна функція меню
def main():
    while True:
        print("\nВиберіть дію:")
        print("1 - Оновити ім'я студента")
        print("2 - Оновити назву курсу")
        print("3 - Видалити студента")
        print("4 - Вийти")
        choice = input("\nВведіть номер дії: ").strip()

        if choice == "1":
            update_student_name()
        elif choice == "2":
            update_course_title()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print("\nВихід.")
            print_all_students_courses()
            break
        else:
            print("\nНевірний вибір. Спробуйте ще раз.")

# Запуск програми
if __name__ == "__main__":
    main()
    session.close()  # Закриваємо сесію після завершення
