""""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    if len(s) != len(t):
        return False
    return collectChars(s) == collectChars(t)
    
def collectChars(word):
    frequencies ={}
    for char in word:
        if char not in frequencies:
            frequencies[char] =1
        else:
            frequencies[char] +=1
    return frequencies

print(isAnagram("anagram","nagaram")) #True
print(isAnagram("rat","car")) #False