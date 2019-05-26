def isPalindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[~i]:
            return False
    return True


w = "dogeeseseegod"
x = isPalindrome(w)
print(x)
