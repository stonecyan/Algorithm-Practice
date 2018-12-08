import numpy


def countIslands(mat):
    islands = 0
    foundIslands = numpy.zeros(shape=(len(mat), len(mat[0])))
    numIslands = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1 and foundIslands[i][j] != 0:
                numIslands += 1
                foundIslands[i][j] += 1
                if mat[i + 1][j] == 1 and i != len(mat):
                    foundIslands[i + 1][j] += 1
                if mat[i - 1][j] == 1 and i != 0:
                    foundIslands[i - 1][j] += 1
                if mat[i][j + 1] == 1 and j != len(mat[0]):
                    foundIslands[i][j + 1] += 1
                if mat[i][j - 1] == 1 and j != 0:
                    foundIslands[i][j - 1] += 1
    return numIslands


# Example 1
# {1, 1, 0, 0, 0},
# {0, 1, 0, 0, 1},
# {1, 0, 0, 1, 1},
# {0, 0, 0, 0, 0},
# {1, 0, 1, 0, 1}
inp = [[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [1, 0, 0, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1]]
print(countIslands(inp))
