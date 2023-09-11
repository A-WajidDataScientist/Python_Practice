# Remove duplicate num from list
l1 = [1, 1, 2, 2, 3, 3, 4, 4]
l = []

for i in l1:
    if i not in l:
        l.append(i)

print(l1, l)
