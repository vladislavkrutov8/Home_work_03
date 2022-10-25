# Задача 3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
n = int(input('Введите размер списка: '))

def get_list_from_input(n):
    str_list = [''] * n
    for i in range(n):
        str_list[i] = float(input(f'Input row {i + 1}: '))

    return str_list

list_length = get_list_from_input(n)

def max_and_min(list_length):
    for i in range(n):
        list_length[i] = (list_length[i]) - (int(list_length[i]))
    return list_length

a = max_and_min(list_length) 
b = max(a) - min(a)
print(f"{max_and_min(list_length)} => {round(b,2)} ")

