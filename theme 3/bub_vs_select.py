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
    
list100 = [random.randint(1,1000) for _ in range(100)]  
list100_sorted = bubble_sort(list100)
print()  

@timing_decorator
def selected_sort(arr):
    n = len(arr)
    for ind in range(n):
        minind = ind
        for j in range (ind+1, n):
            if arr[j] < arr[minind]:
                minind = j
        arr[ind], arr[minind] = arr[minind], arr[ind] 
    return arr

list100_sorted1 = selected_sort(list100)
print()

#сортировка выбором 0.000299
#пузырьковая сортировка 0.000649 

list1000 = [random.randint(1,5000) for _ in range(1000)]
list10000 = [random.randint(1,50000) for _ in range(10000)]

bubble_sort(list100)
bubble_sort(list1000)
bubble_sort(list10000)
print()
selected_sort(list100)
selected_sort(list1000)
selected_sort(list10000)