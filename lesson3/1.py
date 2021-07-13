def my_func(a,b):
    try:
        c=a/b
        return c
    except ZeroDivisionError:
        print("Нельзя делить на ноль")
print(my_func(int(input("Введите делимое:")),int(input("Введите делитель:"))))