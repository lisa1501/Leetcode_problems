"""
Given a string s, return the longest 
palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""
# Time complexity: O(n*n)
# Space complexity: O(n)
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    res = ""
    resLen = 0

    for i in range(len(s)):
        #odd length
        l , r = i, i
        while l >= 0 and r <len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l:r+1]
                resLen = r- l + 1
            l -= 1
            r += 1
        # even length
        l , r = i, i+1
        while l >= 0 and r <len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l:r+1]
                resLen = r- l + 1
            l -= 1
            r += 1

    return res

print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
