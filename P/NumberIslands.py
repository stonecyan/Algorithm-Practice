# Runtime is O(M*N), but worst case could be O((M*N)^2) if whole array is an island
import numpy


def countIslands(mat):
    islands = 0
    foundIslands = numpy.zeros(shape=(len(mat), len(mat[0])))
    numIslands = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1 and foundIslands[i][j] == 0:
                numIslands += 1
                foundIslands[i][j] += 1
                checkNearby(i, j, foundIslands, mat)

    return numIslands


def checkNearby(x, y, fI, mat):
    if mat[x][y] == 0:
        return

    if x < len(fI) - 1:
        if mat[x + 1][y] == 1 and fI[x + 1][y] == 0:
            fI[x + 1][y] += 1
            checkNearby(x + 1, y, fI, mat)
    if x > 0:
        if mat[x - 1][y] == 1 and fI[x - 1][y] == 0:
            fI[x - 1][y] += 1
            checkNearby(x - 1, y, fI, mat)
    if y < len(mat[0]) - 1:
        if mat[x][y + 1] == 1 and fI[x][y + 1] == 0:
            fI[x][y + 1] += 1
            checkNearby(x, y + 1, fI, mat)
    if y > 0:
        if mat[x][y - 1] == 1 and fI[x][y - 1] == 0:
            fI[x][y - 1] += 1
            checkNearby(x, y - 1, fI, mat)

    return fI


# Example 1
# {1, 1, 0, 0, 0},
# {0, 1, 0, 0, 1},
# {1, 0, 0, 1, 1},
# {0, 0, 0, 0, 0},
# {1, 0, 1, 0, 1}
inp = [[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [1, 0, 0, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1]]
print(countIslands(inp))
