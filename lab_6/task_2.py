import math
b = [int(x) for x in input("enter list").split()]

newB = []

for j in b:
    if j % 2 == 0:
        summ = 0
        i = j
        for g in range(1, i+1):
            summ += 1/g
        newB.append(summ)
    else:
        newB.append((math.factorial(j)/2) + 3)

ans = 1

for x in newB:
    if x%2 == 1:
        ans *= x

print(ans)
