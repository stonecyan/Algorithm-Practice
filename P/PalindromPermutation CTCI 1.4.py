#O(n) runtime
def checkPalindrome(str):
    forwards = str
    backwards = str[::-1]
    for i in range(len(str)):
        if forwards[i] != backwards[i]:
            return False
    return True


x = checkPalindrome("asdf")
print(x)
