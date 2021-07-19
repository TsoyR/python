my_list = [12, 2, 3, 1, 8, 5, 4, 8]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num] and num>1]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')
