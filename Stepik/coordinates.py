n = int(input())
count = [0, 0, 0, 0]
names = ['Первая четверть:', 'Вторая четверть:', 'Третья четверть:', 'Четвертая четверть:']
for _ in range(n):
    n = [int(i) for i in input().split(' ')]
    x, y = n[0], n[1]
    if x > 0:
        if y > 0:
            q1 += 1
        elif y < 0:
            q4 += 1

    elif x < 0:
        if y > 0:
            q2 += 1
        elif y < 0:
            q3 += 1

for i in range(4):
    print(names[i], count[i])