import random

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)     

print(fibonacci(5))
print()

def max_el(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        max_el(left)
        max_el(right)
        
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = right[j]
                i += 1
            else:
                arr[k] = left[i]
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

    return arr[-1]

list20 = [random.randint(1,1000) for _ in range(20)]
print(list20)
print()    
print(f'Наибольшее число в списке: {max_el(list20)}')
print()

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

list10 = [random.randint(1,100) for _ in range(10)]
print(list10)
print()        
print(quick_sort(list10))           