""""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], 
you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""

# Time complexity: O(n)
# Space complexity: O(1)

def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    result = 0
    n  = len(nums)
    cur_end, cur_far = 0,0

    for i in range(n-1):
        cur_far = max(cur_far, i + nums[i])# 2,4,4,4,8
        if i == cur_end :
            result += 1 #1,2
            cur_end = cur_far #2,4

    return result

print(jump([2,3,1,1,4]))
print(jump([2,3,0,1,4]))