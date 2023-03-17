# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)

import random

numb_list = [random.randint(0, 10) for _ in range(10)]
count = 0

print(numb_list)
for i in range(len(numb_list) - 1):
    if numb_list[i] < numb_list[i + 1]:
        count += 1

print(count)
