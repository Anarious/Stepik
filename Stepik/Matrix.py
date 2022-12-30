n = int(input())
matrix = [[int(i) for i in input().split(' ')] for _ in range(n)]


sum = 0
for row in matrix:
    for num in row:
        if r == c:
            sum += matrix[r][c]
        print(matrix[r][c], end=' ')
    print()

print(sum)

