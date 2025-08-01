from datetime import datetime

def analyze_heartbeat(input_file="hblog.txt", output_file="hb_test.log"):
    # Ключ, який ідентифікує потрібний потік у логах
    key = "Key TSTFEED0300|7E3E|0400"
    filtered_lines = []

    # Відкриваємо файл і зчитуємо рядки, що містять цей ключ
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            if key in line:
                filtered_lines.append(line.strip())  # Зберігаємо рядок без пробілів з кінця

    timestamps = []
    # Для кожного відфільтрованого рядка шукаємо час у форматі Timestamp HH:MM:SS
    for line in filtered_lines:
        idx = line.find("Timestamp ")
        if idx != -1:
            # Витягуємо 8 символів після слова "Timestamp " — це час у форматі HH:MM:SS
            time_str = line[idx + 10:idx + 18]
            # Перетворюємо рядок у datetime-обʼєкт для подальшої роботи з часом
            time_obj = datetime.strptime(time_str, "%H:%M:%S")
            timestamps.append((time_str, time_obj))

    # Відкриваємо файл для запису результатів аналізу
    with open(output_file, "w", encoding="utf-8") as log:
        # Ідемо по парах послідовних таймстемпів
        for i in range(len(timestamps) - 1):
            t1_str, t1 = timestamps[i]
            t2_str, t2 = timestamps[i + 1]
            # Обчислюємо інтервал у секундах між сусідніми сигналами
            delta = abs((t2 - t1).total_seconds())

            # print(f"{t1_str} -> {t2_str} = {delta} сек")  # перевірка які є випадки

            # Якщо інтервал більше 31 сек, але менше 33 — логування WARNING
            if 31 < delta < 33:
                log.write(f"WARNING at {t2_str}: Heartbeat interval {delta:.1f} seconds\n")
            # Якщо інтервал 33 і більше — логування ERROR
            elif delta >= 33:
                log.write(f"ERROR at {t2_str}: Heartbeat interval {delta:.1f} seconds\n")

if __name__ == "__main__":
    analyze_heartbeat()




