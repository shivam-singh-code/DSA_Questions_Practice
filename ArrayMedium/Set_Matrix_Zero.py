# Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.

# Examples
# Examples 1:

# Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]

# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Explanation: Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.
 
# Input: matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

# Output:[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# Explanation:Since matrix[0][0]=0 and matrix[0][3]=0. Therefore 1st row, 1st column and 4th column will be set to 0

def ZeroMatrix_brute(matrix, n, m):
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                markRow(matrix, n, m, i)
                markCol(matrix, n, m, j)

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    
    return matrix

def markRow(matrix, n, m, i):
    for j in range(m):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def markCol(matrix, n, m, j):
    for i in range(n):
        if matrix[i][j] != 0:
            matrix[i][j] = -1
    

#Better Approach 
def ZeroMatrix_better(matrix, n, m):
    row_marked = [None] * n
    col_marked = [None] * m
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row_marked[i] = 1
                col_marked[j] = 1
    
    for i in range(n):
        for j in range(m):
            if row_marked[i] or col_marked[j]:
                matrix[i][j] = 0
                
    return matrix


def ZeroMatrix_optimal(matrix, n, m):
    col0 = 1
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
            
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] != 0:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
    
    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0 
    
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0
            
    return matrix        

def zeroMatrix(matrix, n, m):
    col0 = 1

    # Step 1: Mark 1st row & column
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0

    # Step 2: Set matrix[i][j] to 0 based on markers
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Step 3: Set first row to 0 if needed
    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0

    # Step 4: Set first column to 0 if needed
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0

    return matrix

matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
n = len(matrix)
m = len(matrix[0])
# print(ZeroMatrix_brute(matrix, n, m))
# print(ZeroMatrix_better(matrix, n, m))
print(ZeroMatrix_optimal(matrix, n, m))
# print(zeroMatrix(matrix, n, m))