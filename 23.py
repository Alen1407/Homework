def is_sorted(ls):
    ls1 = ls.copy()
    ls1.sort()
    if ls == ls1:
        return True
    return False
 
    
print(is_sorted([1,2,3,4]))
