s = [[i] for i in input().split(' ')]

lst = [s[0]]
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        lst.append(s[i])
    elif s[i] == s[i-1]:
        lst[-1].extend(s[i])
print(lst)

