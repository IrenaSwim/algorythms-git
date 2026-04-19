import functools 
import timeit
import random
import time

def timing_decorator(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        exec_time = end_time - start_time 
        print(f'функция {func.__name__} выполнилась за {exec_time} сек')    
        return result 
    return wrapper   

def liner_search(arr, target):
       for ind in range(len(arr)):
           if arr[ind] == target:
               return ind
       return -1
       
#Временная сложность - O(n): время поиска прямо пропорционально размеру входных данных
#Пространственная сложность -О(1): алгоритму требуется постоянный объем памяти

list100 = [random.randint(1, 200) for _ in range(100)]

print(liner_search(list100, 113))
print(liner_search(list100, 57))
print(liner_search(list100, 11))

s = """def func_test():
    arr = [x for x in range(100)]
    liner_search(arr, 44)
"""

print(f'Время выполнения функции для list100: {timeit.timeit(stmt=s, number=50)}')

s1 = """def func_test():
     arr = [x for x in range(10)]
     liner_search(arr, 8)
"""

print(f'Время выполнения функции для list10: {timeit.timeit(stmt=s1, number=50)}')

s2 = """def func_test():
     arr = [x for x in range(10000)]
     liner_search(arr, 6789)
"""

print(f'Время выполнения функции для list1000: {timeit.timeit(stmt=s2, number=50)}')