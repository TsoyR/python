def my_func(x, y, z):
    list_1 = [x, y, z]
    total = []
    max_1 = max(list_1)
    total.append(max_1)
    list_1.remove(max_1)
    max_2 = max(list_1)
    total.append(max_2)
    print(sum(total))

print(my_func(int(input("Введите первый аргумент ")), int(input("Введите второй аргумент ")), int(input("Введите третий аргумент "))))

