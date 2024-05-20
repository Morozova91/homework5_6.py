# Списки и словари
# Работа со списками
my_list = ['apple', 'orange', 'strawberry', 'peach', 'limon', 'coconaut', 'lime']
print(f'List: ', my_list)
first_element = my_list[0]
print(f'First element: ', first_element)
last_element = my_list[-1]
print(f'Last element: ', last_element)
sublist = my_list[3:6]
print(f'Sublist: ', sublist) #  с третьего до пятого элемент
my_list[3] = 'apricot' # Изменение значения третьего элемента
print(f'Modified list: ',my_list)
# Работа со словарями
my_dict = {'apple': 'яблоко', 'orange': 'апельсин', 'strawberry': 'клубника', 'apricot': 'абрикос', 'limon': 'лимон', 'coconaut': 'кокос', 'lime': 'лайм'}
print(f'Dictionary: ' ,my_dict)
print(f'Translation: ', my_dict['orange'])
my_dict['kiwi'] = 'киви'
print(f'Modified dictionary: ', my_dict)
