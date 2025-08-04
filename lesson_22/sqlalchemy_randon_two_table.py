import random
from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

# Проміжна таблиця для зв'язку студентів і курсів
student_courses = Table(
    'student_courses', Base.metadata,
    Column('student_id', ForeignKey('students.id'), primary_key=True),
    Column('course_id', ForeignKey('courses.id'), primary_key=True)
)

# Таблиця студентів
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship('Course', secondary=student_courses,
                           back_populates='students')

# Таблиця курсів
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    students = relationship('Student', secondary=student_courses,
                            back_populates='courses')

# Підключення до бази (тут створюється файл 'students.db')
engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)  # Створюємо таблиці в базі

Session = sessionmaker(bind=engine)

# Весь код, який створює початкові дані і виводить студентів,
# виконується лише якщо файл запускається напряму.
# Якщо цей файл імпортуємо далі як модуль, наприклад у скрипті для додавання студента,
# цей код не виконується і не друкує базу до внесення змін.
if __name__ == "__main__":
    session = Session()

    # Додаємо курси лише якщо їх ще немає
    if not session.query(Course).first():
        course_titles = ['Математика', 'Фізика', 'Інформатика', 'Англійська', 'Історія']
        courses = [Course(title=title) for title in course_titles]
        session.add_all(courses)
        session.commit()

    # Додаємо студентів лише якщо їх ще немає
    if not session.query(Student).first():
        courses = session.query(Course).all()
        for i in range(20):
            student = Student(name=f"Студент_{i+1}")
            # Випадковий вибір 1-3 курсів для студента
            student.courses = random.sample(courses, random.randint(1, 3))
            session.add(student)
        session.commit()

    # Виводимо усіх студентів та їх курси
    students = session.query(Student).all()
    for student in students:
        print(f"{student.name} навчається на курсах:"
              f" {[course.title for course in student.courses]}")

    session.close()
