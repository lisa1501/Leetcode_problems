"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

# Time complexity: O(n) => n=len(nums)
# Space complexity: O(m) => m is the number of unique characters of the input.We need a dictionary to store unique characters.

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    result = 0
    chars = {}
    
    start = 0
    for current_idx in range(n):
        if s[current_idx] not in chars:
            result = max(result, current_idx-start+1)
        else:
            if chars[s[current_idx]] < start:
                result = max(result, current_idx-start+1)
            else:
                start = chars[s[current_idx]]+1

        chars[s[current_idx]] = current_idx

    return result

print(lengthOfLongestSubstring("abcabcbb")) #3
print(lengthOfLongestSubstring("bbbbb")) #1
print(lengthOfLongestSubstring("pwwkew")) #3