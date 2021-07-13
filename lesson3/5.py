def my_calc():

    try:
         entered_list = input("Введите список чисел, разделенных пробелом: ").split()
         new_list = input("Добавьте список чисел, разделенных пробелом: ").split()
    except ValueError:
        return
    num_list = [int(i) for i in entered_list]
    result_list = [int(i) for i in new_list]
    return result_list,num_list
num_list,result_list=my_calc()
print(sum(num_list)+sum(result_list))
