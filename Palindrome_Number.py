"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:

-231 <= x <= 231 - 1
"""
# Time complexity : O(log⁡10(n))
# Space complexity : O(1)
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0 or (x%10==0 and x!=0):
        return False

    reverte_number =0
    while x> reverte_number:
        reverte_number = reverte_number * 10 + reverte_number %10 

        x //= 10
    return x == reverte_number or x == reverte_number//10

print(isPalindrome(121)) #True
print(isPalindrome(-122)) #False
print(isPalindrome(10)) #False