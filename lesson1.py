#1
a: int=20
b=a+30
print(a,b)
name=input("Введите своё имя: ")
print(name)
age=int(input("Введите свой возраст:"))
print(age)
#2
seconds=int(input("Введите время в секундах:"))
print(seconds//360,"чч:",(seconds%360)//60,"мм:",(seconds%360)%60,"cc")
#3
n=(int(input("Введите число: ")))
print(n+n**2+n**3)
#4
number=int(input("Введите целое положительное число: "))
m=number%10
while number>0:
      number=number//10
      if number%10>m:
            m=number%10
print(m)
#5
profit=int(input("Введите выручку фирмы: "))
costs=int(input("Введите издержки фирмы "))

if profit <= costs:
      print("Фирма работает в убыток")
else:
      print("Фирма работает с прибылью. Рентабельность выручки составила:",a)
      worker=int(input("Введите количество сотрудников фирмы: "))
      print("прибыль в расчете на одного сторудника: ",b)
a=profit/costs
b=profit/worker











