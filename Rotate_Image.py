"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = matrix_one
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = matrix_two 
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

matrix_one=[[1,2,3],[4,5,6],[7,8,9]]
matrix_two=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

# Time complexity: O(n) => n = len(matrix)*len(matrix[0])
# Space complexity: O(1)
def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    l = 0
    r = len(matrix) -1
    while l < r:
        matrix[l], matrix[r] = matrix[r], matrix[l]
        l += 1
        r -= 1
    print(matrix)

    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

print(rotate(matrix_one)) #[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
print(rotate(matrix_two)) #[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]