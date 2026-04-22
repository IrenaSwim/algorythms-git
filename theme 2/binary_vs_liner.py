import functools 
import time
import random

def timing_decorator(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        exec_time = end_time - start_time 
        print(f'функция {func.__name__} выполнилась за {exec_time:.6f} сек')    
        return result 
    return wrapper

@timing_decorator
def liner_search(arr, target):
       for ind in range(len(arr)):
           if arr[ind] == target:
               return f'Индекс: {ind}'
       return -1

@timing_decorator
def binary_search(arr, target):
    first = 0
    last = len(arr) - 1
    mid = len(arr) // 2
    while arr[mid] != target and last >= first:
        if arr[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
        mid = (last + first) // 2 
    if last < first:
        return -1
    else:
        return f'Индекс: {mid}'
    
list100 = [random.randint(1,1000) for _ in range(100)]
print(list100)

target = int(input('Введите число для поиска: '))

print(liner_search(list100, target))
print()
print(binary_search(list100, target))
#алгоритм бинарного поиска сработал в 2 раза быстрее.

#собираем данные для графиков
list10 = [x for x in range(1,21) if x % 2 == 0]
biglist = [x for x in range(1,5000) if x % 3 == 0]
hugelist = [x for x in range(1,20000) if x % 2 != 0]

target1 = 18
target2 = 4665
target3 = 13231

print(liner_search(list10, target1))
print()
print(liner_search(biglist, target2))
print()
print(liner_search(hugelist, target3))
print()
print(binary_search(list10, target1))
print()
print(binary_search(biglist, target2))
print()
print(binary_search(hugelist, target3))
print()


