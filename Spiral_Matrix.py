"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = matrix_one
row remains in middle
The bottom nested for loops will traverse (in-order): 6,7

Example 2:
Input: matrix = matrix_two
Single element remains in middle
The bottom nested for loops will traverse (in-order): 5

Example 3:
Input: matrix = matrix_three
Column remains in middle
The bottom nested for loops will traverse (in-order): 5,8

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
matrix_one = [[1,2,3,4],
[5,6,7,8],
[9,0,1,2]]
matrix_two =[[1,2,3],
[4,5,6],
[7,8,9]]
matrix_three=[[1,2,3],
[4,5,6],
[7,8,9],
[0,1,2]]

# Complexity:
# Time complexity:O(m*n)  we traverse all elements in the matrix to be able to return them
# Space complexity:O(m*n) If you don't consider output variable size in your analysis then: O(1) space
def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    m = len(matrix)
    n = len(matrix[0])

    row_start =0
    row_end = m-1
    col_start = 0
    col_end = n-1
    result = []

    while row_start<row_end and col_start<col_end:
        for col in range(col_start,col_end):
            result.append(matrix[row_start][col])
        
        for row in range(row_start,row_end):
            result.append(matrix[row][col_end])
        
        for col in range(col_end,col_start,-1):
            result.append(matrix[row_end][col])
        
        for row in range(row_end,row_start,-1):
            result.append(matrix[row][col_start])
            
        row_start +=1
        col_end-=1
        row_end -=1
        col_start += 1

    if len(result) < m*n:
        for row in range(row_start, row_end+1):
            for col in range(col_start, col_end+1):
                result.append(matrix[row][col])

    return result

print(spiralOrder(matrix_one)) #[1, 2, 3, 4, 8, 2, 1, 0, 9, 5, 6, 7]
print(spiralOrder(matrix_two)) #[1, 2, 3, 6, 9, 8, 7, 4, 5]
print(spiralOrder(matrix_three)) #[1, 2, 3, 6, 9, 2, 1, 0, 7, 4, 5, 8]