def ghost_above(current_row, current_col):
    while current_row > 0:
        current_row -= 1
        if matrix[current_row][current_col] == 0:
            return True
    return False

def solution(matrix):
    
    count = 0
    # save number of rows
    current_row = 0
    rows = len(matrix)
    # save num cols 
    cols = len(matrix[0])

    current_row = 0
    for x in range(rows):
        for y in range(cols):
            if x == 0: 
                if matrix[x][y] != 0:
                    count += matrix[x][y]
            else:
                if matrix[x][y] != 0 and ghost_above(x, y, matrix) == False:
                    count += matrix[x][y]
    return count

print(solution([[1, 1, 1, 0], 
          [0, 5, 0, 1], 
          [2, 1, 3, 10]]))