class HashTable:
    def __init__(self, size):
        self.size = size 
        self.table = [[] for _ in range(size)]
        self.counter = 0
        
    def hash_func(self, key):
        return hash(key) % self.size 
        
    def insert(self, key, value):
        index = self.hash_func(key) 
        self.table[index] = []
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value 
                return
        self.table[index].append([key, value])
        self.counter += 1
        if self.counter / self.size > 0.7:
            self.resize()
        
    def get(self, key):
        index = self.hash_func(key)  
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
        
    def delete(self, key):
        index = self.hash_func(key) 
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                return True
        return False 
        
    def resize(self):
        new_size = self.size * 2
        new_table = [[] for _ in range(new_size)] 
        self.size = new_size
        for index in self.table:
            for pair in index:
                new_index = self.hash_func(pair[0])
                new_table[new_index] = [] 
                for pair in new_table[new_index]:
                    if pair[0] == pair[0]:
                        pair[1] = pair[1]
                        return
                new_table[new_index].append([pair[0], pair[1]])   
        self.table = new_table       
        
htab1 = HashTable(5) 
htab1.insert('one', 1)
htab1.insert('two', 2)
htab1.insert('three', 3)
htab1.insert('four', 4)
htab1.insert('five', 5)
htab1.insert('six', 6)
print(htab1.size)
print(htab1.get('five'))
htab1.insert('seven', 7)
htab1.insert('eight', 8)
print(htab1.size)
print(htab1.counter)