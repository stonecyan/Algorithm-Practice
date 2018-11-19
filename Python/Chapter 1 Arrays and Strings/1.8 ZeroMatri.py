def zeroMatrix(input):
    m = len(input)
    n = len(input[0])
    rows = []
    cols = []

    for i in range(m):
        for j in range(n):
            if input[i][j] == 0:
                rows.append(i)
                cols.append(j)
    print(rows)
    print(cols)
    for row in rows:
        zeroRow(input, row)
    for col in cols:
        zeroColumn(input, col)

    print(input)


def zeroRow(input, row):
    for j in range(len(input[0])):
        input[row][j] = 0


def zeroColumn(input, col):
    for i in range(len(input)):
        input[i][col] = 0


matrix = [[1, 2, 3, 4, 5], [2, 0, 5, 6, 7], [3, 4, 5, 5, 0]]

zeroMatrix(matrix)
