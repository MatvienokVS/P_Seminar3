# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1.N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint as rnd

search_number = int(input('Введите искомое число: '))
count = 0

numb_list = [rnd(1, 5) for i in range(30)]

for j in numb_list:
    if j == search_number:
        count += 1

print(*numb_list)
print(count)
