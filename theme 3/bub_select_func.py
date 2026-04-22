import random 

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
    
list10 = [random.randint(1,100) for _ in range(10)]  
print(list10)
list10_sorted = bubble_sort(list10)  
print(list10_sorted)

def selected_sort(arr):
    n = len(arr)
    for ind in range(n):
        minind = ind
        for j in range (ind+1, n):
            if arr[j] < arr[minind]:
                minind = j
        arr[ind], arr[minind] = arr[minind], arr[ind] 
    return arr
    
list10_sorted = selected_sort(list10) 
print(list10_sorted)        