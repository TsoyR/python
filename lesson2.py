#1
my_list=[1,'F',1.2,True]
for el in my_list:
    print(type(el))


#2
number = int(input("Введите количество элементов списка "))
my_list = []
i = 0
el = 0


for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)






#3
month=int(input("Введите месяц в виде целого числа:"))
my_dict={1:"январь-зима",2:"февраль-зима",3:"март-весна",4:"апрель-весна",5:"май-весна",6:"июнь-лето",7:"июль-лето",8:"август-лето",9:"сентяборь-осень",10:"октябрь-осень",11:"ноябрь-осень",12:"декабрь-зима"}
print(my_dict[month])

my_list=["Зима","Лето","Весна","Осень"]
if month==1 or 2 or 3:
    print(my_list[0])
elif month==3 or 4 or 5:
    print([2])
elif month==6 or 7 or 8:
    print([1])
else:print([3])
#4
string=input("Введите строку из несколько слов разделённых пробелами:")
string1=string.split()
for el in string1:
    print(el[:10])

#5
my_list=[1,5,7,9,8]
number=int(input("Введите число:"))
new_list=[]
for el in my_list:
    print(number)


#6
my_dict = dict({'название': input("введите название "), 'цена': input("Введите цену "),
'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})

my_analys = dict(
        {'название': my_dict.get('название'), 'цена': my_dict.get('цена'), 'количество': my_dict.get('количество'),
         'ед': my_dict.get('ед')})
print(my_list)
print(my_analys)
