"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""
# Time Complexity : O(n)
# Space Complexity : O(n)
def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    return transformString(s) == transformString(t)

def transformString(s):
    chars = {}
    letters =[]
    for i, ch in enumerate(s):
        if ch not in chars:
            chars[ch] = i
        letters.append(str(chars[ch]))

    return "".join(letters)

print(isIsomorphic("egg","add")) #True
print(isIsomorphic("foo", "bar")) #False
print(isIsomorphic("paper", "title")) #True