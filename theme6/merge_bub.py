import random
import time
import functools

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

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr    


list20 = [random.randint(1, 100) for _ in range(20)]
print(list20)
print()
print(merge_sort(list20))
print()

@timing_decorator
def bubble_sort(arr):
    n = len(arr)
    swapped = False
    for ind in range(n):
        for j in range(0, n - ind - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True    
        if not swapped:
            break
    return arr

test1 = [random.randint(1,100) for _ in range(10)]
test2 = [random.randint(1,1000) for _ in range(100)]
test3 = [random.randint(1,10000) for _ in range(1000)]
test4 = [random.randint(1,100) for _ in range(10)]
test5 = [random.randint(1,1000) for _ in range(100)]
test6 = [random.randint(1,10000) for _ in range(1000)]

start_time = time.time()
merge_sort(test1)
end_time = time.time()
print(f'Функция merge_sort выполнена за {(end_time - start_time):.6f}')
start_time = time.time()
merge_sort(test2)
end_time = time.time()
print(f'Функция merge_sort выполнена за {(end_time - start_time):.6f}')
start_time = time.time()
merge_sort(test3)
end_time = time.time()
print(f'Функция merge_sort выполнена за {(end_time - start_time):.6f}')
print()
bubble_sort(test4)
bubble_sort(test5)
bubble_sort(test6)
#Временная сложность сортировки слиянием в худшем случае O(n log n), пузырьковой - O(n^2).
#Исходя из тестового времени, на достаточно небольших массивах (до 100) пузырьковая сортировка
#работает чуть быстрее. Однако, для больших массивов предпочтительна сортировка слиянием (в несколько десятков раз быстрее).