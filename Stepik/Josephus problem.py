n, k = int(input()), int(input())

my_list = [i for i in range(1, n+1)]
count = 0
while len(my_list) != 1:
    for _ in range(k-1):
        temp = my_list.pop(0)
        my_list.append(temp)
    my_list.pop(0)
print(*my_list)


