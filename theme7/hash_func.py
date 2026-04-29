def hash_str(str):
    hash_value = 0
    for char in str:
        hash_value += ord(char)
    return hash_value 
    
str_dict = {} 

for _ in range(3):
     
    while True:
        string = input('Введите ключ-строку: ') 
        if string not in str_dict:
            s_hash = hash_str(string)
            str_dict.setdefault(string, s_hash) 
            break
        else:
            print('Такой ключ уже существует.') 
print(str_dict) 
print()

def dict_insert(dict, str_key):
    if str_key in dict:
        return f'Такой ключ уже существует.'
    else:
        key_hash = hash_str(str_key) 
        str_dict.setdefault(str_key, key_hash) 
        return f'Ключ {str_key} добавлен в соварь со значением {key_hash}.'
        
def get_value(dict, key):
    if key in dict:
        return dict[key]      
    return f'Ключ {key} отсутствует в словаре'
    
str1 = input('Введите строку: ')
print()
print(dict_insert(str_dict, str1))
print(get_value(str_dict, str1))