""""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

# Time Complexity : O(m)=>Creating a HashMap of counts for the magazine is O(m)O(m)O(m),
# Space Complexity : O(1)
import collections
def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str 
    :type magazine: str
    :rtype: bool
    """
    if len(ransomNote) > len(magazine):
        return False

    letters = collections.Counter(magazine)
    print(letters)
    for c in ransomNote:
        if letters[c] <= 0:
            return False
        letters[c] -=1
    return True

print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("aa","aab"))