"""
Given a character array s, reverse the order of the words.
A word is defined as a sequence of non-space characters. 
The words in s will be separated by a single space.
Your code must solve the problem in-place, i.e. without allocating extra space.

Example 1:
Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

Example 2:
Input: s = ["a"]
Output: ["a"]

Constraints:

1 <= s.length <= 105
s[i] is an English letter (uppercase or lowercase), digit, or space ' '.
There is at least one word in s.
s does not contain leading or trailing spaces.
All the words in s are guaranteed to be separated by a single space.

"""

#helper function
def reverse(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
        
# Time complexity: O(n)
# Space complexity: O(1)
def reverseWords(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    # reverse input data by calling helper function
    reverse(s, 0, len(s) - 1)
    #two pointers, beginning and walking by iterating
    beg = 0
    for i in range(len(s)):
        #if current index is empty str, call helper function revese from beginning to walking pointer
        if s[i] == ' ':
            reverse(s, beg, i-1)
            # set new beginning to next index
            beg = i + 1
        # if current index is the last index
        elif i == len(s) -1:
            reverse(s, beg, i)
    return s

print(reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))
print(reverseWords(["a"]))



