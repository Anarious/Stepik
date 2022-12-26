def pascal(n):
    res = ''
    list1 = []
    for i in range(n):
        temp_list = []
        for j in range(i+1):
            if j ==0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(list1[i-1][j-1] + list1[i-1][j])
        list1.append(temp_list)
    for row in list1:
        for i in row:
            res += str(i) + ' '
        res += '\n'
    return res[:-1]


n = int(input('Enter the row number: '))
print(pascal(n))
