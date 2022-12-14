lst = [1, 5, 2, 3, 4, 6, 1, 7]
res = []
i = 0
k = 0
for j, item in enumerate(lst):
    res.append([item])
    print(res)
    for i in range(j, len(lst)):
        if lst[i] > res[j][k]:
            res[j].append(lst[i])
            k += 1
    k = 0
print(res)
