n = int(input("enter n: "))
ans = 0

while n:
    if (n%10 == 0):
        ans += 1
    n //= 10

print(ans)
   
