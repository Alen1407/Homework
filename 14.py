ls = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
ls_gaps = [ls[i+1]-ls[i] for i in range(len(ls)-1)]
print(ls_gaps)
print(max(ls_gaps))
two_quantity = 0
for x in ls_gaps:
    if x == 2:
        two_quantity += 1

print("The percentage of gaps that have size 2: " + str(two_quantity*100/len(ls_gaps)) + "%")

