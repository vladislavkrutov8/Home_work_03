# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

n = int(input('Введите размер списка: '))

def get_list_from_input(n):
    str_list = [''] * n
    for i in range(n):
        str_list[i] = int(input(f'Input row {i + 1}: '))

    return str_list

list = get_list_from_input(n)
new_list = []
for i in range(len(list)):
    while i < len(list)/2 and n > len(list)/2:
        n = n - 1
        a = list[i] * list[n]
        new_list.append(a)
        i += 1

print(f" {list} => {new_list}")
