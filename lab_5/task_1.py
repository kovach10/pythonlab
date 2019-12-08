import math

a = float(input("enter a: "))
n = int(input("enter n: "))
ans = 0

for i in range(n):
    ans += math.log(math.fabs(a**(n-i)))

print(ans)
