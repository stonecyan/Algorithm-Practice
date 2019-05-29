def baseConversion(number, b1, b2):
    negative = False
    if number[0] == "-":
        negative = True
        number = number[1:len(number)]
    numberAsInt = int(number)
    baseTen = 0
    x = 0
    for i in range(len(number) - 1, -1, -1):
        baseTen += int(number[x]) * b1 ** i
        x += 1
    ntwo = ""
    nleftover = baseTen
    while nleftover > b2:
        ntwo = ntwo + str(nleftover % b2)
        nleftover = nleftover // b2
    ntwo = ntwo + str(nleftover % b2)
    final = str(nleftover // b2)
    if final != "0":
        ntwo = ntwo + final

    if negative:
        ntwo = ntwo + "-"

    return ntwo[::-1]


x = baseConversion("13346", 10, 7)
print(x)
