ls = [[0, 'M', 0, 'M', 0],
      [0,  0, 'M', 0,  0],
      [0,  0,  0,  0,  0],
      ['M','M',0,  0,  0],
      [0,  0,  0, 'M', 0]]

ls_res = []
for i in range(5):
    ls_res.append([])
    for j in range(5):
        if ls[i][j] == 'M':
            ls_res[i].append('M')
        else: ls_res[i].append(0)


