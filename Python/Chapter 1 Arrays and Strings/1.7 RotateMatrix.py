def RotateMatrix(input):
    n = len(input)
    for column in range(n // 2):
        first = column
        last = n - column - 1
        for i in range(first, last):
            top = input[column][i]
            # right to bottom
            matrix[][]
