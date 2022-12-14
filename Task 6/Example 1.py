with open('file.txt', 'r') as f:
    lst_1 = f.read()
lst = " ".join(list(filter(lambda x: not 'абв' in x, lst_1.split())))

print(lst_1)

print(lst)
