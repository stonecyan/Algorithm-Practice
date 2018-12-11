import copy


def combinationSum(numbers, target):
    combinations = []
    combination = []
    getCombo(numbers, target, 0, combination, combinations)
    return combinations


def getCombo(numbers, target, index, combo, allCombos):
    if target == 0:
        allCombos.append(combo)
        return

    if target < 0:
        return

    for i in range(index, len(numbers)):
        combo.append(numbers[i])
        getCombo(numbers, target - numbers[i], i, combo, allCombos)
        combo.pop()


x = combinationSum([2, 3, 7], 7)
x1 = combinationSum([2, 3, 5], 8)
print(x)
print(x1)
