arr = [float(x) for x in input("enter list: ").split()]
mult = 1
for i in arr:
    mult *= i
    
print(mult**(1/len(arr)))
