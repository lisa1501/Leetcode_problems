"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
"""

# Time complexity: O(n) => n=len(nums)
# Space complexity: O(1)
def minSubArrayLen(target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    start  = 0
    min_size = float('inf')

    current_sum = 0

    for end, num in enumerate(nums):
        current_sum += num
        while current_sum >= target:
            min_size = min(min_size, end-start+1)
            current_sum -= nums[start]
            start += 1
    
    if min_size == float('inf'):
        return 0
    else:
        return min_size
    
print(minSubArrayLen(7, [2,3,1,2,4,3])) #2
print(minSubArrayLen(11,[1,1,1,1,1,1,1,1])) #0
