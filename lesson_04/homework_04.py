adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")
"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")


# task 02 ==
""" Замініть .... на пробіл
"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

import re

# один або більше пробільних символів змінюємо на один
adwentures_of_tom_sawer = re.sub(r"\s+", " ", adwentures_of_tom_sawer).strip()


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

print(f'Літера "h" зустрічається у тексті {adwentures_of_tom_sawer.count("h")} раз.')


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

adwentures_of_tom_sawer_big_letter = adwentures_of_tom_sawer.split()

count = 0

for word in adwentures_of_tom_sawer_big_letter:
    if word.istitle():
        count += 1

print(f"З Великої літери у тексті починається {count} слів.")


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

index_1= adwentures_of_tom_sawer.find("Tom")

# використовуємо початковий індекс наступний після index_1
index_2 = adwentures_of_tom_sawer.find("Tom", index_1+1)

# виводимо позицію, не індекс
print(f'Позиція, на якій слово "Tom" зустрічається вдруге: {index_2+1}.')


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

import re

# ділимо змінну по кінцю речення (., !, ?)
adw_of_tom_sawer_sentences_not_clean = re.split(r'[.!?]', adwentures_of_tom_sawer)

# прибираємо зайві пробіли та останнє пусте речення ''
adwentures_of_tom_sawer_sentences = []

for sentence in adw_of_tom_sawer_sentences_not_clean:
    sentence = sentence.strip()
    if sentence != '':
        adwentures_of_tom_sawer_sentences.append(sentence)

print(adwentures_of_tom_sawer_sentences)


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

print(adwentures_of_tom_sawer_sentences[3].lower())


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

count = 0

for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        count +=1

if count >= 1:
    print("Yes")
else:
    print("No")


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

last_sentences = adwentures_of_tom_sawer_sentences[-1].split()

print(len(last_sentences))
