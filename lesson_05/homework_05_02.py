people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

# Додаємо свій новий запис на початок існуючого списку
people_records.insert(0, ('David', 'Joy', 21, 'Student', 'Arizona'))

# У модифікованому списку обмінюємо елементи з індексами 1 і 5 (1<->5)
people_records[1], people_records[5] = people_records[5], people_records[1]
for index, record in enumerate(people_records):
    print(f"'Індекс': {index}  {record}")

# Перевіряємо, чи всі люди в новому списку з індексами 6, 10, 13 мають вік ≥ 30
person1 = people_records[6]
person2 = people_records[10]
person3 = people_records[13]

if person1[2] >= 30 and person2[2] >= 30 and person3[2] >= 30:
    print("Усі перевірені люди мають вік 30 років або більше:")
else:
    print("Не всі перевірені люди мають вік 30 років або більше:")

print(
    f"{people_records[6]}\n"
    f"{people_records[10]}\n"
    f"{people_records[13]}\n"
    )