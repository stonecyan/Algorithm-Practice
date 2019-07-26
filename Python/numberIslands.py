def numberIslands(array):
    largest island
    islands = 0;
    rows = len(array)
    cols = len(array[0])
    visited = [[False for j in range(cols)]for i in range(rows)]

    for row in range(len(rows)):
        for col in range(len(cols)):
            visited[row][col] = True

            ---if array[row][col] == 1 and visited[row][col] == False:

                islands += 1
                checkIslands(row, col, array, visited)

    return islands


def checkIslands(row, col, array, visited):
    islandSize
    if col < cols - 1:
        if array[row][col + 1] == 1 and visited[row][col + 1] == False:
            visited[row][col + 1] = True
            checkIslands(row, col + 1, array, visited)
    if col > 0:
         if array[row][col - 1] == 1 and visited[row][col - 1] == False:
             visited[row][col - 1] = True
             checkIslands(row, col - 1, array, visited)
     if row<rows-1:
        if array[row+1][col]==1 and visited[row+1][col]==False:
            visited[row+1][col]=True
            checkIslands(row+1, col, array, visited)
    if row>0:
        if array[row-1][col]==1 and visisted[row-1][col]==False:
            visited[row-1][col]=True
            checkIslands(row-1, col, array, visited)
