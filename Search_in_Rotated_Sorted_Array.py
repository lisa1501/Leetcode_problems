"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""

#Time complexity : O(logN)
#Space complexity : O(1)

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l = 0
    r = len(nums)-1

    while l <= r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid

        if nums[mid]>=nums[l]:
            if target>=nums[l] and target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if target <= nums[r] and target > nums[mid]:
                l = mid+1
            else:
                r = mid-1
    return -1

print(search(nums = [4,5,6,7,0,1,2], target = 0))#4
print(search(nums = [4,5,6,7,0,1,2], target = 3))#-1
print(search(nums = [1], target = 0))#-1