# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        intervals = self.intervals
        if not intervals:
            intervals.append(Interval(val, val))
        else:
            self.intervals = self.insertInterval(intervals, val)
            
    # if there are lots of merge, each merge cause shift of array, which time complexity is O(n)    
    def insertInterval(self, intervals, val):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []
        flag = False
        for interval in intervals:
            if interval.start <= val and interval.end >= val:
                return intervals
            elif interval.end < val-1:
                res.append(interval)
                
            elif interval.end == val - 1:
                res.append(Interval(interval.start, val))
                flag = True
            elif interval.start > val + 1:
                if not flag:
                    res.append(Interval(val, val))
                    flag = True
                res.append(interval)
            elif interval.start == val + 1:
                if flag:
                   res[-1].end = interval.end
                else:
                    res.append(Interval(val, interval.end))
                    flag = True
        if not res:
            res.append(Interval(val, val))
        else:
            if res[-1].end < val - 1:
                res.append(Interval(val, val))
        return res
        

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
