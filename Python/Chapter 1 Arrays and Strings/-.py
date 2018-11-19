def checkPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    string1 = list(s1)
    string2 = list(s2)
    string1.sort()
    string2.sort()
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            return False
    return True


x = checkPermutation("asdf", "sade")
print(x)
