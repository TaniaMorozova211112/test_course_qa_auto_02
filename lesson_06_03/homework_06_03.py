lst_1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

lst_2 = []

for variable_str in lst_1:
    if isinstance(variable_str, str):
        lst_2.append(variable_str)

print(lst_2)
