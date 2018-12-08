def stringCompression(input):
    compressedString = []
    count = 0
    for i in range(len(input)):
        if i != 0 and input[i] != input[i - 1]:
            compressedString.append(input[i - 1] + str(count))
            count = 0
        count += 1
    compressedString.append(input[-1] + str(count))
    return ''.join(compressedString)


ex = "aabbccAA"
x = stringCompression(ex)
print(x)
