#O(N*N!)
def recursivePermutations(str):
    if len(str) <= 1:
        return set([str])

    lastChar = str[-1]
    allMinusLast = str[:-1]

    allMinusLastPermutations = recursivePermutations(allMinusLast)

    perms = set()

    for permutations in allMinusLastPermutations:
        for i in range(len(allMinusLast) + 1):
            permutation = (
                permutations[:i]
                + lastChar
                + permutations[i:]
            )
            perms.add(permutation)

    return perms


x = recursivePermutations("asdf")
print(x)
