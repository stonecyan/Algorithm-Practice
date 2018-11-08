def Palindrome(input):
    forward = list(input)
    backward = list(reversed(input))
    i = 0
    while i < len(input):
        if forward[i] != backward[i]:
            return False
        else:
            i += 1
            continue
    return True


x = Palindrome("asdf")
print(x)
