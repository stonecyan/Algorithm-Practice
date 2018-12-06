# Brute force solution O(n^2) runtime, space O(1)
def subLargestSum(arr):
    maxSum = float("-inf")
    for i in range(len(arr)):
        subSum = 0
        for j in range(i, len(arr)):
            subSum += arr[j]
            if subSum > maxSum:
                maxSum = subSum
    return maxSum

# Sliding window solution


def subLargestSumSliding(arr):


test = [-2, 4, -1, -2, 1, 5, -3, -15, 2, 3]
x = subLargestSum(test)
print(x)
#[1,4,16,21]
