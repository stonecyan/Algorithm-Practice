def uniqueCharacters(input):
    charList = list(input)
    charList.sort()
    i = 0
    while i < len(charList):
        if i == len(charList) - 1:
            return True
        if charList[i] != charList[i + 1]:
            i += 1
            continue
        else:
            return False


asdf = uniqueCharacters("abccde")
print(asdf)
