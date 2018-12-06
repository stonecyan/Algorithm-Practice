import heapq


def kthLargestSort(arr, k)
    arr.sort()
    n = len(arr)
    return arr[n - k]
# Runtime O(nlogn), Space O(1)


def kthLargestNon(arr, k):
    heap = []
    for x in arr:
        heapq.heappush(heap, -x)
    for i in range(k):
        result = heapq.heappop(heap)

    return result * -1


arr = [5, 2, 1, 3, 4, 5]
r = kthLargest(arr, 4)
print(r)

#Non-optimal Solution: Max Heap, Runtime O(nlogn)
#Optimal Solution: Use a min heap with k elements or max heap with n-k+1 elements, Runtime O(nlogk) or O(nlogn-k+1)
#Best Solution: Use min heap with k elements if k < n/2 and max heap with n-k+1 elements if k >= n/2
