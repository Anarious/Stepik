string = input().split(' ')
number = int(input())

def chunked(string, number):
    lst = []

    for i in range(0, len(string), number):
        lst.append(string[i:i+number])

    return lst

print(chunked(string, number))
