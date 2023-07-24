"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
"""

# Time complexity: O(n*m) 
# Space complexity: O(n+m) 
def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    
    n =len(matrix)
    m=len(matrix[0])
    set_rows = set()
    set_cols = set()

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                set_rows.add(i)
                set_cols.add(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in set_rows or j in set_cols:
                matrix[i][j] = 0
    return matrix

print(setZeroes([[1,1,1],[1,0,1],[1,1,1]])) #[[1, 0, 1], [0, 0, 0], [1, 0, 1]]
print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])) #[[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]