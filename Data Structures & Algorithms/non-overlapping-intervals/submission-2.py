class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        temp = [intervals[0]]
        for start, end in intervals[1:]:
            last_start, last_end = temp[-1]
            if start < last_end:
                temp[-1] = [last_start, min(end, last_end)]
                count += 1
            else:
                temp[-1] = [start, end] 
        return count