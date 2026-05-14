class Product:
    def __init__(self, name, category, price, weight, description):
        self.name = name
        self.category = category 
        self.price = price
        self.weight = weight
        self.description = description 
        
    def info(self):
        return {'name':self.name, 'category':self.category, 'price':self.price, 'weight':self.weight, 'description':self.description}   
        
    def __str__(self):
        return f'{self.description} "{self.name}", вес {self.weight} гр., цена {self.price}'  
        
    def edit(self):
        try:
            while True:
                change = input('Напишите, что вы хотите изменить: name, category, price, weight, description ')
                if change.lower() == 'name':
                    new = input('Введите новое название ') 
                    if not new.isalpha():
                        raise TypeError('В названии не должно быть цифр')
                    self.name = new
                    after = input('Хотите внести другие изменения? (да/ нет) ')
                    if after == 'нет':
                        break
                elif change.lower() == 'category':
                    new = input('Введите новую категорию ') 
                    if not new.isalpha():
                        raise TypeError('В названии не должно быть цифр')
                    self.category = new
                    after = input('Хотите внести другие изменения? (да/ нет) ')
                    if after == 'нет':
                        break
                elif change.lower() == 'price':
                    new = int(input('Введите новую цену '))
                    if new < 0:
                        raise ValueError('Цена не должна быть отрицательной')   
                    self.price = new
                    after = input('Хотите внести другие изменения? (да/ нет) ')
                    if after == 'нет':
                        break
                elif change.lower() == 'weight':
                    new = int(input('Введите новый вес '))
                    if new < 0:
                        raise ValueError('Вес не должен быть отрицательным')   
                    self.weight = new
                    after = input('Хотите внести другие изменения? (да/ нет) ')
                    if after == 'нет':
                        break
                elif change.lower() == 'description':
                    new = input('Введите новое описание ')
                    if len(new) > 60:
                        raise ValueError('Описание превышает допустимую длину')
                    self.description = new
                    after = input('Хотите внести другие изменения? (да/ нет) ')
                    if after == 'нет':
                        break
                else:
                    print(f'Параметр {change} отсутствует')   
                    break   
        except ValueError as err:
            print(err)
        except TypeError as err:
            print(err) 

def quick_sort_product(arr, mole, reverse=False):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2] 
    if reverse == False and mole == 'price':
        left = [x for x in arr if x.price < pivot.price] 
        middle = [x for x in arr if x.price == pivot.price]
        right = [x for x in arr if x.price > pivot.price]
        return quick_sort_product(left, 'price') + middle + quick_sort_product(right, 'price')
    elif reverse == True and mole == 'price':
        left = [x for x in arr if x.price > pivot.price] 
        middle = [x for x in arr if x.price == pivot.price]
        right = [x for x in arr if x.price < pivot.price]
        return quick_sort_product(left, 'price', True) + middle + quick_sort_product(right, 'price', True)
    elif reverse == False and mole == 'weight':
        left = [x for x in arr if x.weight < pivot.weight] 
        middle = [x for x in arr if x.weight == pivot.weight]
        right = [x for x in arr if x.weight > pivot.weight]
        return quick_sort_product(left, 'weight') + middle + quick_sort_product(right, 'weight')
    else:
        left = [x for x in arr if x.weight > pivot.weight] 
        middle = [x for x in arr if x.weight == pivot.weight]
        right = [x for x in arr if x.weight < pivot.weight]
        return quick_sort_product(left, 'weight', True) + middle + quick_sort_product(right, 'weight', True)
    
def merge_sort_product(arr, mole, reverse=False):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]      
        right = arr[mid:]
        if mole == 'price' and reverse == False:
            merge_sort_product(left, 'price')
            merge_sort_product(right, 'price')
        elif mole == 'price' and reverse == True:
            merge_sort_product(left, 'price', True)
            merge_sort_product(right, 'price', True)
        elif mole == 'weight' and reverse == False:
            merge_sort_product(left, 'weight')
            merge_sort_product(right, 'weight')
        else:
            merge_sort_product(left, 'weight', True)
            merge_sort_product(right, 'weight', True)
        
        i = j = k = 0
        
        if mole == 'price' and reverse == False:
            while i < len(left) and j < len(right):
                if left[i].price < right[j].price:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]  
                    j += 1
                k += 1
        elif mole == 'price' and reverse == True:
            while i < len(left) and j < len(right):
                if left[i].price > right[j].price:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]  
                    j += 1
                k += 1
        elif mole == 'weight' and reverse == False:
            while i < len(left) and j < len(right):
                if left[i].weight < right[j].weight:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]  
                    j += 1
                k += 1
        else:
            while i < len(left) and j < len(right):
                if left[i].weight > right[j].weight:
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

class Cart:
    def __init__(self):
        self.products = []
        
    def add_product(self, product:Product):
        self.products.append(product) 
    
    def delete_product(self, product:Product):
        self.products.remove(product) 
    
    def show_cart(self):
        for product in self.products:
            print(product)  
        
    def bubble_sort(self, mole, reverse=False):
            n = len(self.products)
            if mole == 'price':
                for i in range(n):
                    swapped = False
                    for j in range(0, n - i - 1):
                        if reverse == False:
                            if self.products[j].price > self.products[j + 1].price:
                                self.products[j], self.products[j + 1] = self.products[j + 1], self.products[j]    
                                swapped = True
                        else:
                            if self.products[j].price < self.products[j + 1].price:
                                self.products[j], self.products[j + 1] = self.products[j + 1], self.products[j]    
                                swapped = True
                    if not swapped:
                        break    
            else:
                for i in range(n):
                    swapped = False
                    for j in range(0, n - i - 1):
                        if reverse == False:
                            if self.products[j].weight > self.products[j + 1].weight:
                                self.products[j], self.products[j + 1] = self.products[j + 1], self.products[j]    
                                swapped = True
                        else:
                            if self.products[j].weight < self.products[j + 1].weight:
                                self.products[j], self.products[j + 1] = self.products[j + 1], self.products[j]    
                                swapped = True
                    if not swapped:
                        break    
                 
    def quick_sort(self, mole, reverse=False):
        m = mole
        n = reverse
        self.products = quick_sort_product(self.products, m, n) 
    
    def merge_sort(self, mole, reverse=False):
        m = mole
        n = reverse
        merge_sort_product(self.products, m, n)
    
    def insert_sort(self, mole, reverse=False):
        arr = self.products 
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            if mole == 'price' and reverse == False:
                while j >= 0 and arr[j].price > key.price:
                    arr[j + 1] = arr[j]
                    j -= 1
            elif mole == 'price' and reverse == True:
                while j >= 0 and arr[j].price < key.price:
                    arr[j + 1] = arr[j]
                    j -= 1
            elif mole == 'weight' and reverse == False:
                while j >= 0 and arr[j].weight > key.weight:
                    arr[j + 1] = arr[j]
                    j -= 1
            else:
                while j >= 0 and arr[j].weight < key.weight:
                    arr[j + 1] = arr[j]
                    j -= 1
            arr[j + 1] = key
            
        self.products = arr
        
    def total_price(self):
        return sum(x.price for x in self.products)  
                 
class OnlineShop:
    def __init__(self):
        self.catalogue = {}
        
    def add_product(self, product:Product):
        self.catalogue.setdefault(product, product.info())   
        
    def delete_product(self, name):
        counter = 0
        for key, value in self.catalogue.items():
            if value['name'] == name:
                del self.catalogue[key]
                break
            else: 
                counter += 1
        if counter == len(self.catalogue):           
            print(f'Товар отсутствует в каталоге') 
    
    def show_catalogue(self):
        print('Какая категория вас интересует?\nсерьги\nбраслет\nожерелье\nкольцо\nвсе')
        cat = input('Напишите категорию: ')
        if cat == 'все':
            for key in self.catalogue.keys():
                print(key)
                print('----')
        else:
            for key, value in self.catalogue.items():
                if value['category'] == cat:
                    print(key)
                    print('----')
        
    def add_to_cart(self, cart:Cart, name):
        counter = 0
        for key, value in self.catalogue.items():
            if value['name'] == name:
                cart.add_product(key)
                print(f'Товар {name} добавлен в корзину')
                break
            else:
                counter += 1
        if counter == len(self.catalogue):              
            print(f'Товар {name} отсутствует в каталоге')      

    def in_cart(self, cart:Cart):
        agreement = input('Хотите пропустить сортировку товаров в корзине? Введите да или нет ') 
        print()   
        if agreement == 'да':
            cart.show_cart()
        else:
            mole = input('Отсортировать товары по цене (введите price) или по весу (введите weight): ') 
            print()
            reverse = input('Отсортировать по возраcтанию (введите False) или по убыванию (введите True)')  
            print()
            print('Выбрать алгоритм сортировки:\nпузырьковая (введите 1)\nбыстрая (введите 2)\nслиянием (введите 3)\nвставками (введите 4)')
            way = int(input())
            if way == 1:
                if mole == 'price' and reverse == False:
                    cart.bubble_sort('price')
                elif mole == 'price' and reverse == True:   
                    cart.bubble_sort('price', True)
                elif mole == 'weight' and reverse == False:
                    cart.bubble_sort('weight')    
                else:
                    cart.bubble_sort('weight', True) 
                return cart.show_cart()     
            elif way == 2:
                if mole == 'price' and reverse == False:
                    cart.quick_sort('price')
                elif mole == 'price' and reverse == True:   
                    cart.quick_sort('price', True)
                elif mole == 'weight' and reverse == False:
                    cart.quick_sort('weight')    
                else:
                    cart.quick_sort('weight', True) 
                return cart.show_cart()            
            elif way == 3:
                if mole == 'price' and reverse == False:
                    cart.merge_sort('price')
                elif mole == 'price' and reverse == True:   
                    cart.merge_sort('price', True)
                elif mole == 'weight' and reverse == False:
                    cart.merge_sort('weight')    
                else:
                    cart.merge_sort('weight', True) 
                return cart.show_cart()       
            else:
                if mole == 'price' and reverse == False:
                    cart.insert_sort('price')
                elif mole == 'price' and reverse == True:   
                    cart.insert_sort('price', True)
                elif mole == 'weight' and reverse == False:
                    cart.insert_sort('weight')    
                else:
                    cart.insert_sort('weight', True)
                return cart.show_cart()            
                

        
prod_set = [
    Product('bugs', 'серьги', 1100, 14, 'Серебряные серьги в виде жуков'),
    Product('rose bud', 'браслет', 940, 50, 'Серебряный браслет с застежкой в виде розы'),
    Product('birds', 'серьги', 3500, 25, 'Золотые серьги в виде птиц'),
    Product('ivy', 'ожерелье', 2200, 150, 'Серебряное ожерелье-цепочка'), 
    Product('tulip', 'кольцо', 800, 12, 'Серебряное кольцо с цветком тюльпана')
]   
#     Product('cherries', 'браслет', 4000, 35, 'Золотой браслет-цепочка с подвесками'),
#     Product('orchard', 'ожерелье', 1300, 140, 'Серебряное ожерелье-цепочка с деревянными вставками'),
#     Product('bee', 'кольцо', 4100, 50, 'Золотое кольцо с пчелкой'),
#     Product('drops', 'серьги', 750, 30, 'Серебряные серьги в виде капель'),
#     Product('suns', 'серьги', 6800, 100, 'Золотые серьги в виде солнц'), 
#     Product('leave', 'кольцо', 1200, 22, 'Серебряное кольцо в виде свернутого листа'),
#     Product('snake', 'браслет', 950, 60, 'Золотой браслет в виде змейки')
# ]    

cart1 = Cart()
shop1 = OnlineShop()
for product in prod_set:
    shop1.add_product(product)
#shop1.show_catalogue()    
print()   
shop1.delete_product('cherries') 
#shop1.show_catalogue()
print()
shop1.add_to_cart(cart1,'drops')
shop1.add_to_cart(cart1,'tulip')
shop1.add_to_cart(cart1,'leave')
shop1.add_to_cart(cart1,'birds')
shop1.add_to_cart(cart1,'ivy')
shop1.add_to_cart(cart1,'fox')
print()
cart1.show_cart()
shop1.in_cart(cart1)

  
# for product in prod_set:
#     cart1.add_product(product)
# cart1.bubble_sort('price', True)
# #print(cart1.total_price())

# # cart1.merge_sort('weight') 
# cart1.show_cart()
    
