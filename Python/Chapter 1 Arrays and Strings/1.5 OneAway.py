def OneAway(s1, s2):
    if len(s1) == len(s2):
        return Replace(s1, s2)
    if len(s1) - 1 == len(s2):
        return InsertRemove(s1, s2)
    if len(s1) + 1 == len(s2):
        return InsertRemove(s1, s2)
    return False


def Replace(s1, s2):
    edit = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if edit == True:
                return False
            edit = True
    return True


def InsertRemove(s1, s2):
    i = 0
    j = 0
    edited = False
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited == True:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True


x = OneAway("ace", "b")
print(x)
