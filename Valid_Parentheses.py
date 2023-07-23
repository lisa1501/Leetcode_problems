"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

# Time complexity: O(n)
# Space complexity: O(n)
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    mapping = {'(':')', '{':'}','[':']'}
    stack =[]

    for char in s:
        if char in mapping:
            stack.append(char)
        elif len(stack)==0 or mapping[stack.pop()]!= char:
            return False
        
    return len(stack) == 0

print(isValid("()")) #True
print(isValid("()[]{}")) #True
print(isValid("(]")) #False
