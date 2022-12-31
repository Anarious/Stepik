xy = input()
x = 'abcdefgh'.index(xy[0])
y = '87654321'.index(xy[1])
print(x, y)
matrix = [['.' for _ in range(8)] for _ in range(8)]

matrix[y][x] = 'N'

for i in range(8):
    for j in range(8):
        if (y - i) ** 2 + (x - j) ** 2 == 5:
            matrix[i][j] = '*'

for r in range(8):
    for c in range(8):
        print(matrix[r][c], end=' ')
    print()
