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


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [] 
        right = []  
        mid = []
        for item in arr:
            if item < pivot:
                left.append(item)  
            elif item > pivot:
                right.append(item)   
            else:
                mid.append(item) 
                
        return quick_sort(left) + mid + quick_sort(right)
    
def insertion_sort(arr):
    for ind in range(1, len(arr)):
        key = arr[ind]
        j = ind - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr        