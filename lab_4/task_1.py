import math
a = int(input("Введіть сторони трикутника: "))
b = int(input("Введіть сторони трикутника: "))
c = int(input("Введіть сторони трикутника: "))
if a>0 and b>0 and c>0:
    p = (a+b+c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("S= ",s)
else:
    print("Введено не правильну сторону")
