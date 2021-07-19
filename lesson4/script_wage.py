from sys import argv

script,a, b, c= argv
print(script)
print("выработка в часах: ",a)
print("ставка в час: ", b)
print("премия: ", c)
res=int(a)*int(b)+int(c)
print("Заработная плата сотрудника",res)