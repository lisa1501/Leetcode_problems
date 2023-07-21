"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
# Time complexity: O(n)
# Space complexity: O(n)
def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    longest_streak = 0
    nums_set = set(nums)

    for num in nums_set:
        if num -1 not in nums_set:
            current_num = num
            current_streak = 1

            while current_num+1 in nums_set:
                current_num +=1
                current_streak += 1
            
            longest_streak = max(longest_streak,current_streak)

    return longest_streak

print(longestConsecutive([100,4,200,1,3,2])) #4
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1])) #9
