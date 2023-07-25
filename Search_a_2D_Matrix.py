"""
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

# Time Complexity : O(log(m*n))
# Space Complexity : O(1)
def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """

    m = len(matrix)
    n = len(matrix[0])
    
    l =0
    r = m*n-1

    while l<=r :
        mid = (r+l)//2
        mid_ele = matrix[mid//n][mid%n]
        
        if mid_ele == target:
            return True
        elif mid_ele>target :
                r = mid-1
        else:
            l = mid+1

    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3)) #True
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13)) #False