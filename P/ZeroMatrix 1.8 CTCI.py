def zeroMatrix(mat):
    zeroRow = []
    zeroCol = []
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if mat[row][col] == 0:
                zeroRow.append(row)
                zeroCol.append(col)
    for r in zeroRow:
        makeRowZero(mat, r)
    for c in zeroCol:
        makeColZero(mat, c)

    return mat


def makeRowZero(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0


def makeColZero(matrix, col):
    for j in range(len(matrix)):
        matrix[j][col] = 0


inp = [[1, 1, 1, 0, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
print(zeroMatrix(inp))
