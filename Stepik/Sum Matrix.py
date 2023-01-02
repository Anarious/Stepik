n, m = [int(i) for i in input().split()]

matrix1 = [[int(i) for i in input().split(' ')] for _ in range(n)]
input()
matrix2 = [[int(i) for i in input().split(' ')] for _ in range(n)]

for r in range(n):
    for c in range(m):
        print(matrix1[r][c] + matrix2[r][c], end=' ')
    print()