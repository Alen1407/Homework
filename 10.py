def perfNum(x):
    res = 0
    for i in range(1,x):
        if x%i==0:
            res += i
    if res == x:
        return True
    else:
        return False

for i in range(1,10000):
    if perfNum(i):
        print(i)
    
