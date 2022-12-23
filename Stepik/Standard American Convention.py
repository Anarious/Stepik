n = int(input())
n = list(str(n))


if len(n) > 3:
    for i in range(len(n), 0, -3):
        n.insert(i, ',')
    print(*n[:-1], sep='')
else:
    print(*n, sep='')

# OR SIMPLY BELOW:
# num = int(input())
# print(f'{num:,}')

