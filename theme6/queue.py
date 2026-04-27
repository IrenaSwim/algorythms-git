import time
import random
from datetime import datetime

class Queue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
        
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0) 
        else:
            return f'Пустая очередь'    
            
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return f'Пустая очередь'  
    
    def size(self):
        return len(self.items)#нужен для моделирования        
        
q1 = Queue()   
 
print('Моделирование очереди печати')  
print()
for i in range(1, 4):
    doc = f'doc_{i}.pdf'
    q1.enqueue(doc)
    print(f'Поступил файл {doc}. Всего в очереди {q1.size()}') 
    time.sleep(random.uniform(0.5, 1))  
print()        
print('Работает принтер')  
print()
while True:
    current_doc = q1.dequeue()
    print(f'Печатается файл {current_doc}')
    time.sleep(random.uniform(1, 2))
    print(f'Печать завершена в {datetime.now().strftime("%H:%M%:%S")}')
    if q1.is_empty():
        break
print()

print('Очередь печати пуста. Принтер готов к работе')    
