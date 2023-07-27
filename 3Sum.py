"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
# Time Complexity: O(n^2)
# Space Complexity: from O(log⁡n) to O(n), 
                # depending on the implementation of the sorting algorithm. 
                # For the purpose of complexity analysis, we ignore the memory required for the output.
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()
    n = len(nums)

    for i in range(n-2):
        if i > 0 and nums[i]==nums[i-1]:
            continue
        
        l = i+1
        r = n-1
        while l < r:
            s = nums[i]+nums[l]+nums[r]
            if s < 0:
                l+=1
            elif s>0:
                r-=1
            else:
                res.append((nums[i],nums[l],nums[r]))
                while l <r and nums[l]==nums[l+1]:
                    l+=1
                while l < r and nums[r]==nums[r-1]:
                    r-=1
                l +=1
                r -=1
    return res
print(threeSum([-1,0,1,2,-1,-4]))#[(-1, -1, 2), (-1, 0, 1)]
print(threeSum([0,1,1]))#[]
print(threeSum([0,0,0]))#[(0, 0, 0)]