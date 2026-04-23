import random 

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1) 

n = 6
print(f'Факториал числа {n}: {factorial(n)}') 
print()

def sum_list_rec(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum_list_rec(arr[1:])  
    
list = [3, 4, 5, 6, 7] 
print(f'Сумма чисел списка: {sum_list_rec(list)}') 
print()  

def binary_search_recursive(arr, low, high, targ):
    if high > low:
        mid = (low + high) // 2
        if arr[mid] == targ:
            return mid
        elif arr[mid] < targ:
            return binary_search_recursive(arr, mid+1, high, targ)
        else:
            return binary_search_recursive(arr, low, mid-1, targ)   
    return -1
    
list10 = sorted([random.randint(1,100) for _ in range(10)])
print(list10) 
targ = int(input('Введите число: ')) 
print(f'Идекс числа {targ}: {binary_search_recursive(list10, 0, 10, targ)}') 
print(f'Интекс числа 101: {binary_search_recursive(list10, 0, 10, 101)}') 
print()

class Stack:
    def __init__(self):
        self.stack = []
        
    def is_empty(self):
        return len(self.stack) == 0
        
    def push(self, item):
        self.stack.append(item) 
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return 'Список пуст'  
            
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return 'Список пуст'
            
stack1 = Stack()   
stack1.push('model')
stack1.push('capacity')
stack1.push('settings')
print(stack1.peek())
stack1.pop()
print(stack1.peek())