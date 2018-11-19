def uniqueCharacters(input):
    inputset = set(input)
    if len(inputset) != len(input):
        return False
    else:
        return True


asdf = uniqueCharacters("abccde")
print(asdf)
