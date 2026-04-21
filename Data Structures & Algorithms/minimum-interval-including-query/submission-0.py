class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = [0]*len(queries)
        for j  in range(len(queries)):
            minLength = float('inf')
            for i in range(len(intervals)):
                if queries[j] in range(intervals[i][0], intervals[i][1]+1):
                    length =  intervals[i][1] - intervals[i][0] + 1
                    minLength = min(minLength, length)
            if minLength == float('inf'):
                res[j] = -1
            else:
                res[j] = minLength
        return res