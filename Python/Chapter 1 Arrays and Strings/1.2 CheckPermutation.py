def CheckPermutation(string1, string2):
    if len(string1) != len(string2):
        return False
    charList1 = list(string1)
    charList2 = list(string2)
    charList1.sort()
    charList2.sort()
    i = 0
    while i < len(charList1):
        if charList1[i] != charList2[i]:
            return False
        else:
            i += 1
            continue
    return True


asdf = CheckPermutation("god", "dog")
print(asdf)
