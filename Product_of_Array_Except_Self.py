"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]


Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

"""

# Time complexity: O(n)
# Space complexity: O(1)

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    result = [1]*n 
    #result = [1,1,1,1]
    #nums =   [1,2,3,4]


    for i in range(1,n):
        result[i] = nums[i-1] * result[i-1]
    print(result)#[1, 1, 2, 6]
    right = 1
    for i in reversed(range(n)):
        result[i] = result[i] * right
        right *= nums[i]
        
    return result

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))