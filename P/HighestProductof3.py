# Runtime complexity is O(n)
def highestProductThree(arr):
    highest = highest2 = highest3 = float("-inf")
    lowest = lowest2 = lowest3 = float("inf")
    i = 0
    while i < len(arr):
        if i > 1:
            if highest2 * arr[i] > highest3:
                highest3 = highest2 * arr[i]
            if lowest2 * arr[i] > highest3:
                highest3 = lowest2 * arr[i]
        if i > 0:
            if highest * arr[i] > highest2:
                highest2 = highest * arr[i]
            if lowest * arr[i] < lowest2:
                lowest2 = lowest * arr[i]
        if arr[i] > highest:
            highest = arr[i]
        if arr[i] < lowest:
            lowest = arr[i]
        i += 1
    return highest3


a = [-5, -6, 1, 2, 3, 4]
b = [1, 2, 3, 4, 5]
c = [-5, 1, 2, 3]
x = highestProductThree(c)
print(x)
