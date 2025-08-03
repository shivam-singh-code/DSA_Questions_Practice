# Problem Statement: Given a Matrix, print the given matrix in spiral order.

# Examples:

# Example 1:
# Input: Matrix[][] = { { 1, 2, 3, 4 },
# 		      { 5, 6, 7, 8 },
# 		      { 9, 10, 11, 12 },
# 	              { 13, 14, 15, 16 } }

# Outhput: 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10.
# Explanation: The output of matrix in spiral form.

# Example 2:
# Input: Matrix[][] = { { 1, 2, 3 },
# 	              { 4, 5, 6 },
# 		      { 7, 8, 9 } }
			    
# Output: 1, 2, 3, 6, 9, 8, 7, 4, 5.
# Explanation: The output of matrix in spiral form.

def SpiralMatrix(matrix, n, m):
    top = 0
    left = 0
    right = m-1
    bottom = n-1

    spiraled_list = []
    
    
    while(top <= bottom and left <= right):
        # Move from left to right
        for i in range(left, right+1):
            spiraled_list.append(matrix[top][i])
        
        top += 1
        
        # Move from top to bottom
        for i in range(top, bottom + 1):
            spiraled_list.append(matrix[i][right])
        
        right -= 1
        
        # Move right to left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                spiraled_list.append(matrix[bottom][i])
            bottom -= 1
        
        # Move from bottom to top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                spiraled_list.append(matrix[i][left])
            left += 1
        
    return spiraled_list
    

matrix = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

n = len(matrix)
m = len(matrix[0])

print(SpiralMatrix(matrix, n, m))
# 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10