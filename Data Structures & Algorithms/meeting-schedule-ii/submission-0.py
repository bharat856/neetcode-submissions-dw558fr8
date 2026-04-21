"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for currentMeeting in intervals:
            time.append((currentMeeting.start, 1))
            time.append((currentMeeting.end, -1))
        
        time.sort(key = lambda x :(x[0], x[1]))
        count = res = 0
        for t in time:
            count += t[1]
            res = max(count, res)
        return res
                