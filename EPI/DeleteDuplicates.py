def deleteDuplicates(list):
    if not list:
        return 0
    replace = 1
    for i in range(1, len(list)):
        if list[replace - 1] != list[i]:
            list[replace] = list[i]
            replace += 1
    del list[replace:]
    return list


a = [2, 3, 5, 5, 7, 11, 11, 11, 13]
x = deleteDuplicates(a)
print(x)
