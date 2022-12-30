n = int(input())
matrix = [input().split() for _ in range(n)]


for r in range(n):
    for c in range(n):
        if matrix[r][c] != matrix[c][r]:
            exit(print('NO'))
else:
    print('YES')
