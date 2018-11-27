def isMember(words, query):
    match = False
    for i in words:
        if sameWord(i, query):
            return True
    return False


def sameWord(s1, s2):
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s2[i] != s1[i] and s2[i] != ".":
            return False
    return True


words = ["foo", "bar", "baz"]

print(isMember(words, "baz"))  # true  (because 'foo' exists in the list of words)
print(isMember(words, "hello"))  # false (because 'hello' does NOT exists in the list of words)

print(isMember(words, "f.o"))   # true  (because the '.' matches the first 'o' in foo)
print(isMember(words, ".."))    # false (no two letter words)

print(isMember(words, ".az"))   # True
