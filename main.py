def write_array_to_file(arr, filename):
    with open(filename, 'w') as f:
        for item in arr:
            f.write(str(item) + '\n')


from random import *
import time

a = [randint(1, 1000) for i in range(int(input('Введите количество случайных чисел: ')))]
write_array_to_file(a, 'Изначальный файл')

c = 0


def shellSort(arr):
    global c
    d = len(arr) // 2
    while d > 0:
        for i in range(d, len(arr)):
            j = i
            while j >= d and arr[j] < arr[j - d]:
                arr[j], arr[j - d] = arr[j - d], arr[j]
                j -= d
                c += 1
        d //= 2
    return arr


start = time.time()
b = shellSort(a)
end = time.time()
print('Количество секунд ', end - start)
print('Количество итераций ', c)
write_array_to_file(b, 'отсортированный файл')

