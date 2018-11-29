def singleNumber(self, nums):
    array = []
    for i in nums:
        if i not in array:
            array.append(i)
        else:
            array.remove(i)
    return array[0]
