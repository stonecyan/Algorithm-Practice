def URLify(input, length):
    output = ""
    i = 0
    for char in input:
        if i >= length:
            break
        if char == " ":
            output += "%20"
        else:
            output += char
        i += 1
    print(output)


URLify("Hello World!       ", 12)
