def reduce_functools(func, ls):
    res = ls[0]
    for item in ls[1:]:
        res = func(res, item)
    return res
    
print(reduce_functools((lambda x, y: x*y), [1,2,3,4]))

def reduce_itertools(func, ls):
    res = [ls[0]]
    i = 0
    for item in ls[1:]:
        res.append(func(res[i], item))
        i += 1
        
    return res
        
print(reduce_itertools((lambda x, y: x*y), [1,2,3,4]))
