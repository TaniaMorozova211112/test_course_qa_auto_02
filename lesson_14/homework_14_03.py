import os
import logging
import xml.etree.ElementTree as ET  # Модуль для роботи з XML-файлами

# Налаштування логування: повідомлення рівня INFO в консолі
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def find_incoming_timing_by_group_number(group_number):
    """
    Функція шукає у файлі groups.xml групу з певним номером
    та повертає значення <timingExbytes>/<incoming>, якщо воно існує.
    """

    # Отримуємо поточну директорію, де знаходиться цей файл .py
    current_dir = os.path.dirname(__file__)

    # Переходимо на один рівень вище (тобто з lesson_14 на test_course_qa_auto_02)
    parent_dir = os.path.dirname(current_dir)

    # Формуємо шлях до XML-файлу, з урахуванням структури папок
    xml_path = os.path.join(
        parent_dir,
        "automation_qa", "ideas_for_test", "work_with_xml", "groups.xml"
    )

    # Перевіряємо, чи існує файл за цим шляхом
    if not os.path.isfile(xml_path):
        logging.error(f"Файл не знайдено: {xml_path}")
        return None  # Повертаємо None, якщо файл відсутній

    # Парсимо XML-файл (завантажуємо дерево елементів)
    tree = ET.parse(xml_path)
    root = tree.getroot()  # Отримуємо кореневий тег (має бути <groups>)

    group_found = False  # Прапорець, щоб відстежити, чи знайдена група

    # Перебираємо всі теги <group> в XML
    for group in root.findall('group'):
        # Шукаємо під тегом <group> тег <number>
        number_elem = group.find('number')

        # Перевіряємо, що тег <number> існує і його текст відповідає номеру
        if number_elem is not None and number_elem.text == str(group_number):
            group_found = True  # Ми знайшли потрібну групу

            # Шукаємо тег <timingExbytes> всередині цієї групи
            timing_exbytes = group.find('timingExbytes')
            if timing_exbytes is not None:
                # Усередині <timingExbytes> шукаємо <incoming>
                incoming_elem = timing_exbytes.find('incoming')
                if incoming_elem is not None:
                    incoming_value = incoming_elem.text  # Отримуємо значення
                    logging.info(f'Group {group_number} incoming timing: {incoming_value}')
                    return incoming_value  # Повертаємо знайдене значення
                else:
                    # Якщо <incoming> відсутній
                    logging.info(
                        f'Group {group_number} знайдена,'
                        f' але відсутній <incoming> у <timingExbytes>.'
                    )
            else:
                # Якщо <timingExbytes> відсутній
                logging.info(
                    f'Group {group_number} знайдена, '
                    f'але відсутній елемент <timingExbytes>.'
                )
            return None  # Закінчуємо перевірку після знайденої групи

    # Якщо не знайдено жодної групи з таким номером
    if not group_found:
        logging.info(f'Group {group_number} не знайдена взагалі')
    return None  # Нічого не знайшли — повертаємо None


# Тестуємо функцію на різних group_number: від 0 до 5
if __name__ == "__main__":
    find_incoming_timing_by_group_number(0)  # Є timingExbytes/incoming
    find_incoming_timing_by_group_number(1)  # Немає timingExbytes
    find_incoming_timing_by_group_number(2)  # Є timingExbytes/incoming
    find_incoming_timing_by_group_number(3)  # Взагалі немає такої групи
    find_incoming_timing_by_group_number(4)  # Є timingExbytes/incoming
    find_incoming_timing_by_group_number(5)  # Є timingExbytes/incoming