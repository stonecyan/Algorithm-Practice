# O(N*N!)


def getPermutations(s):
    if len(s) <= 1:
        return set([s])

    last = s[-1]
    restofLetters = s[:-1]

    lettersMinusLast = getPermutations(restofLetters)

    permutations = set()

    for permutation in lettersMinusLast:
        for i in range(len(permutation) + 1):
            p = permutation[:i] + last + permutation[i:]
            permutations.add(p)

    return permutations


x = getPermutations("asdf")
print(x)
