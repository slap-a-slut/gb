src = [2, 2, 1, 323, 44, 13, 553, 4, 443, 14, 12, 45]
a = {}
for i in src:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1
result = [el for el in src if a[el] == 1]
print(result)
