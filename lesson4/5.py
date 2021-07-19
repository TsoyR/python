from functools import reduce
my_list=[number for number in range(100,1000) if number%2==0]
def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el

print(reduce(my_func, my_list))

