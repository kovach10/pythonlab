n = int(input("enter n: "))
arr = [float(input()) for x in range(n)]
a = float(input("enter a: "))
ans = []
for x in arr:
    ans.append(x*a)
print(ans)
