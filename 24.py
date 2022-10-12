def merge(ls1, ls2):
    ls_res = []
    i = 0
    j = 0
    
    while i < len(ls1) and j < len(ls2):
        if ls1[i] > ls2[j]:
            ls_res.append(ls2[j])
            j += 1
        else:
            ls_res.append(ls1[i])
            i += 1
        
    
    if j >= len(ls2):
        for k in range(i, len(ls1)):
            ls_res.append(ls1[k])
    else:
        for k in range(j, len(ls2)):
            ls_res.append(ls2[k])
    

            
    return ls_res        
    
print(merge([10,12,14, 17], [2,4,6]))
