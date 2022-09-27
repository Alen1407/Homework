x = int(input("Enter the year: "))
res = (abs(x-1600)//4)+1-(abs(x-1600)//100)+abs(x-1600)//400
print(res)
