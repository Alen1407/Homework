ls = [[2,3,9,9,5],
      [10,2,3,11,5],
      [1,9,3,7,6],
      [1,7,9,9,6],
      [4,2,2,0,9]]


dic = {}

for i in range(5):
    for j in range(5):
        if str(ls[i][j]) in dic.keys():
            dic[str(ls[i][j])] += 1
        else:
            dic[str(ls[i][j])] = 1


print(dic)

def max_values_inDic(dic):
    ls = []
    for x in dic.keys():
        ls.append(dic[x])
    ls_max = []
    for i in range(3):
        ls_max.append(max(ls))
        ls.remove(max(ls))

    return ls_max

print(max_values_inDic(dic))

for x in dic:
    if dic[x] in max_values_inDic(dic):
        print(x)
