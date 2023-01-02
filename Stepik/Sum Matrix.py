n, m = [int(i) for i in input().split()]

matrix1 = [[int(i) for i in input().split(' ')] for _ in range(n)]
input()
l, k = [int(i) for i in input().split()]
matrix2 = [[int(i) for i in input().split(' ')] for _ in range(l)]
matrix3 = [[0 for _ in range(k)] for _ in range(n)]

for x in range(n):
    for r in range(k):
        for c in range(l):
            matrix3[x][r] += matrix1[x][c] * matrix2[c][r]
        print(matrix3[x][r], end=' ')
    print()
