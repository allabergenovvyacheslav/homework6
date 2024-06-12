my_dict = {'Myhail': 1980, 'Aleksey': 1985, 'Tatyana': 1990}
print(my_dict)
print(my_dict.get('Tatyana'))
print(my_dict.get('Oleg', "Этот ключ отсутствует"))
my_dict.update({'Vyktor': 1991, 'Aleks': 1992})
print(my_dict)
del my_dict['Tatyana'] # это один из вариантов удаления пары из словаря
print(my_dict)
a=my_dict.pop('Aleksey') # это второй вариант удаления пары из словаря, но этот метод позволяет
                       # возвращать данные, если мы поместим их в переменную (например "a")
print(a)
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

my_set = {12, 12, 12, 34, 43, 'Aleksey', 'Sergey', 'Sergey'}
print(my_set)
my_set.update({'Elena', 2024, (1,2,2,3,1)})
print(my_set)
my_set.remove(12) # удаление из множества элемента "12"
print(my_set)
print(my_set.discard('Elena')) # удаление элемента "Елена"
print(my_set)