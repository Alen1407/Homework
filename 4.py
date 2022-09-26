n = int(input("Enter a number: "))
res = 0
while(n!=0):
   res += n%10
   n = int(n/10)

print(res)
