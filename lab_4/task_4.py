import math
x = int(input("input x: "))
n = int(input("input n: "))
if x<n or x == n:
    y = math.log10(x)-n
else:
    y = math.cos(n*x)
print("y={0}".format(round(y,2)))