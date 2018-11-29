def reverseString(s):
    string = "".join(reversed(s))
    return string


def reverseStringFast(s):
    return s[::-1]


def reverseStringSlow(s):
    string = ""
    for i in s:
        string = i + string
    return string
