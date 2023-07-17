"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
"""

# Time complexity: O(n) => n = len(t)
# Space complexity: O(1)

def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    s_start, s_end = 0, len(s)
    t_start, t_end = 0, len(t)

    while s_start < s_end and t_start < t_end:

        if s[s_start] == t[t_start]:
            s_start +=1

        t_start +=1
        
    return s_start == s_end


print(isSubsequence("abc","ahbgdc")) #True
print(isSubsequence("axc","ahbgdc")) #False