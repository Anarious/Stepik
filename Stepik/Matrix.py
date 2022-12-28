n, m = int(input()), int(input())
matrix = [[input() for _ in range(m)] for _ in range(n)]

for r in range(n):
    for c in range(m):
        print(matrix[r][c], end=' ')
    print()
for r in range(m):
    for c in range(n):
        print(matrix[c][r], end=' ')
    print()