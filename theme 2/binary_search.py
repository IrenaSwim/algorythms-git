import random 

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
        
arr = [x for x in range(20) if x % 2 == 0]
print(arr) 
target = int(input('Введите число: '))
print(binary_search(arr, target)) 
print()
#Времеенная сложность алгоритма - O(log n), где n - число элементов списка.
#Сложность такова, потому как на каждом шаге поиска внутри цикла функции
#пространство поиска уменьшается вдвое.
#Пространственная сложность - О(1) так как реализация поиска итеративная(используем цикл).
#Это значит, что используется постоянный объем доп памяти - создаём лишь 3 переменные
#для отслеживания границ поиска(first, last) и среднего элемента (mid).


list100 = [random.randint(1,1000) for _ in range(100)] 
list100.sort()
print(list100)
print()
numbs = input('Введите 3 числа для поиска через пробел: ')
numbs_list = numbs.split(' ')
target1 = int(numbs_list[0])
target2 = int(numbs_list[1])
target3 = int(numbs_list[2])

result1 = binary_search(list100, target1)
result2 = binary_search(list100, target2)
result3 = binary_search(list100, target3)
print()
print(f'Индекс {target1}: {result1}\nИндекс {target2}: {result2}\nИндекс {target3}: {result3}')
