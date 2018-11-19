import collections


def checkPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    str1 = list(s1)
    str2 = list(s2)
    str1.sort()
    str2.sort()
    i = 0
    while i < len(str1):
        if str1[i] != str2[i]:
            return False
        else:
            i += 1
    return True


def checkPermutationTwo(s1, s2):
    counter = collections.Counter()
    for i in s1:
        counter[i] += 1
    for i in s2:
        if counter[i] == 0:
            return False
        counter[i] -= 1
    return True


x = checkPermutation("sad", "das")
print(x)
y = checkPermutationTwo("asdf", "fdsa")
print(y)
