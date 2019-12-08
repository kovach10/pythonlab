n = int(input("enter n: "))
x0 = x1 = 1

if n == 0 or n == 1:
    print(x1)
else:
    for j in range(n-1):
        xn = x1 + 2 * x0
        x0 = x1
        x1 = xn
    print(xn)
