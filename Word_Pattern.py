"""
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Constraints:
1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""

# Time complexity: O(n) 
# Space complexity: O(1)

def wordPattern(pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """
    words = s.split(' ')
    map_word = {}

    if len(pattern) != len(words) :
        return False
    if len(set(pattern)) != len(set(words)):
        return False

    for i in range(len(words)):
        if words[i] not in map_word:
            map_word[words[i]] = pattern[i]
        elif map_word[words[i]] != pattern[i]:
            return False
    return True

print(wordPattern("abba", "dog cat cat dog")) #True
print(wordPattern("abba", "dog cat cat fish")) #False
print(wordPattern("aaaa", "dog cat cat dog")) # False