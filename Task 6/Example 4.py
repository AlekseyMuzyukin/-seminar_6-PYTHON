lst = lst = list(map(int, input("Введите числа через пробел:\n").split()))
temp = len(lst) // 2 + 1 if len(lst) % 2 != 0 else len(lst) // 2
lst_2 = [lst[i] * lst[len(lst) - i - 1] for i in range(temp)]
print(lst, lst_2)
