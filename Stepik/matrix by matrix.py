n = int(input())

matrix1 = [[int(i) for i in input().split(' ')] for _ in range(n)]

m = int(input())

matrix2 = [[0 for _ in range(n)] for _ in range(n)]

for b in range(m):
    for x in range(n):
        for r in range(n):
            for c in range(n):
                matrix2[x][r] += matrix1[x][c] * matrix2[c][r]
            print(matrix2[x][r])
        print()



