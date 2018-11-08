def StringCompressed(input):
    count = 0
    compressed = []
    for i in range(len(input)):
        if i != 0 and input[i] != input[i - 1]:
            compressed.append(input[i - 1] + str(count))
            count = 0
        count += 1
    compressed.append(input[len(input) - 1] + str(count))
    return ''.join(compressed)


print(StringCompressed("abcccc"))
