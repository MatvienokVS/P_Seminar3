# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint as rnd

value_list = int(input('Введите количество элементов в массиве: '))
numb_list = [rnd(0, 5) for i in range(int(value_list))]
search_numb = list(map(int, numb_list))

X = int(input('Введите искомое число Х: '))
min = X - search_numb[0]
index = 0
for i in range(1, value_list):
    count = X - search_numb[i]
    if count < min:
        min = count
        index = i
print(*numb_list)
print(f'Число {search_numb[index]} в списке наиболее близко по величине к числу {X}')
