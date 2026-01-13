a = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

def get_sign(x):
    if x[0] in '+-':
        return x[0]
i = 0
while i < len(a):
    sign = get_sign(a[i])
    if a[i].isdigit() or (sign and a[i][1:].isdigit()):
        if sign:
            a[i] = sign + a[i][1:].zfill(2)
        else:
            a[i] = a[i].zfill(2)

        a.insert(i, '"')
        a.insert(i + 2, '"')
        i += 2

    i += 1

print(*a)