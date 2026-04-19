import timeit

def liner_search(arr, target):
       for ind in range(len(arr)):
           if arr[ind] == target:
               return ind
       return -1
       
#Временная сложность - O(n): время поиска прямо пропорционально размеру входных данных
#Пространственная сложность -О(1): алгоритму требуется постоянный объем памяти

list100 = [12, 23, 427, 64, 7, 19, 22, 1, 29, 123,
           72, 325, 11, 8, 43, 10, 255, 0, 14, 3,
           222, 31, 89, 111, 323, 108, 2, 55, 544, 71,
           46, 91, 18, 742, 423, 101, 5, 33, 901, 1000,
           202, 24, 122, 206, 531, 999, 17, 3, 80, 303,
           121, 238, 447, 62, 777, 192, 228, 105, 26, 1231,
           721, 327, 112, 8, 43, 10, 255, 0, 14, 3,
           222, 2201, 897, 711, 383, 1081, 297, 555, 5441, 721,
           40, 914, 158, 7421, 400, 100, 509, 3344, 961, 1111,
           2102, 240, 1229, 216, 521, 899, 107, 3111, 20, 30
           ]

target1 = 383
target2 = 323
target3 = 14

result1 = liner_search(list100, target1)
result2 = liner_search(list100, target2)
result3 = liner_search(list100, target3)

print('Примеры использования линейного поиска в list100:')
print(f'Индекс элемента {target1}: {result1}')
print(f'Индекс элемента {target2}: {result2}')
print(f'Индекс элемента {target3}: {result3}')


s = """def func_test():
    arr = [x for x in range(100)]
    liner_search(arr, 44)
"""

print(f'Время выполнения функции для list100: {timeit.timeit(stmt=s, number=100)}')

s = """def func_test():
     arr = [x for x in range(10)]
     liner_search(arr, 8)
"""

print(f'Время выполнения функции для list10: {timeit.timeit(stmt=s, number=100)}')

s = """def func_test():
     arr = [x for x in range(10000)]
     liner_search(arr, 8990)
"""

print(f'Время выполнения функции для list1000: {timeit.timeit(stmt=s, number=100)}') 