"""
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.

Example 2:
Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.

Constraints:

0 <= a, b, c <= 100
a + b + c > 0
"""
# Time complexity: O(nlgn)
# Space complexity: O(n)

import heapq

def longestDiverseString(a, b, c):
    """
    :type a: int
    :type b: int
    :type c: int
    :rtype: str
    """
    result = ''
    arr = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
    heapq.heapify(arr)

    while True:
        count, char = heapq.heappop(arr)
        
        if count == 0: break

        if result and result[-1] == char:
            count1, char1 = heapq.heappop(arr)
            if count1 == 0: break
            result += char1
            count1 += 1
            heapq.heappush(arr, (count, char))
            heapq.heappush(arr, (count1, char1))
        else:
            result += char * min(-count, 2)
            count += min(-count, 2)
            heapq.heappush(arr, (count, char))
            
    return result

print(longestDiverseString(1, 1, 7))#ccaccbcc
print(longestDiverseString(7, 1, 0))#aabaa