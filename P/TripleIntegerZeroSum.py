# Brute force solution, O(n^3) runtime
def ZeroSum(arr):
    combinations = []
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] + arr[k] == 0:
                    combo = [arr[i], arr[j], arr[k]]
                    combinations.append(combo)
    return combinations


def ZeroSumDict(arr):
    combinationz = []
    twoSums = {}
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            twoSum = arr[i] + arr[j]
            twoSums[twoSum] = [arr[i], arr[j]]
    for k in range(len(arr)):
        if -k in twoSums:
            combo = [k, twoSums[-k][0], twoSums[-k][1]]
            combinationz.append(combo)
    return combinationz


x = [5, 3, 0, 1, 2, -5, -3]
a = ZeroSum(x)
b = ZeroSumDict(x)
print(a)
print(b)
