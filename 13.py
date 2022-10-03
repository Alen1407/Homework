def isPolindrome(num):
    return str(num) == str(num)[::-1]

ls = [x for x in range(100, 1000) if isPolindrome(x)]
print(ls)
