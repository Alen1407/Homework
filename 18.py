x = int(input("Enter hour: "))
s = input("am (1) or pm (2)?: ")
dic = {'1':'am', '2':'pm'}
hour_ahead = int(input("How many hours ahead?: "))
x += hour_ahead
if x>12:
    s = '1' if s == '2' else '2'
    x -= 12

print("New hour: {0} {1}".format(x, dic[s]))
