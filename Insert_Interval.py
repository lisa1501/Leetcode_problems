"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""
#solution1
# Time complexity: O(nlogn)
# Space complexity: O(nlogn) or O(n)

#solution2
# Time complexity: O(n) 
# Space complexity: O(1)
def insert(intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    #solution1
    # merged=[]
    # intervals.append(newInterval)
    # intervals.sort(key = lambda x: x[0])
    # for interval in intervals:
    #     if not merged or merged[-1][-1] < interval[0]:
    #         merged.append(interval)
    #     else:
    #         merged[-1][-1]=max(merged[-1][-1], interval[-1])
    # return merged

    #solution2
    start, end = newInterval[0], newInterval[1]
    left, right = [], []
    for i in intervals:
        if i[1] < start:
            left += i,
        elif i[0] > end:
            right += i,
        else:
            start = min(start, i[0])
            end = max(end, i[1])
    return left + [[start, end]] + right

print(insert([[1,3],[6,9]], [2,5]))#[[1, 5], [6, 9]]
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))#[[1, 2], [3, 10], [12, 16]]