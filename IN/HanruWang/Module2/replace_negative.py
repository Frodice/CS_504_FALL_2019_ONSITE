def replace_negtive(listNum):
    for i in range(len(listNum)):
        if listNum[i] < 0:
            listNum[i] = abs(listNum[i])
    return listNum

original = [8, 20, -10, 0, 55, -777]
print(replace_negtive(original))

