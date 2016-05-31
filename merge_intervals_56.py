class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        #intervals = sorted(intervals)
        intervals.sort(key = lambda x:x.start)
        res = []
        res.append(Interval(intervals[0].start, intervals[0].end))
        for i in range(1, len(intervals)):
            # starting in not None guaranteed
            prev = res[-1]
            cur = intervals[i]
            if prev.end < cur.start:
                res.append(Interval(cur.start, cur.end))
            else:
                # merge
                if prev.end >= cur.end:
                    continue
                else:
                    prev.end = cur.end
        return res

# second round
# merge intervals
class Solution2(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
            
        def mycmp(i1, i2):
            if i1.start != i2.start:
                return i1.start - i2.start
            else:
                return i1.end - i2.end
                
        intervals.sort(cmp=mycmp)
        res = []
        for i in range(len(intervals)):
            # starting in not None guaranteed
            if not res:
                res.append(Interval(intervals[i].start, intervals[i].end))
                continue
            prev_interval = res[-1]
            cur_interval = intervals[i]
            if prev_interval.end < cur_interval.start:
                res.append(Interval(cur_interval.start, cur_interval.end))
            else:
                # does the ending boundary equal to the starting boundary counting as same interval after merging?
                # merge
                
                # case check
                if prev_interval.end >= cur_interval.end:
                    continue
                else:
                    prev_interval.end = cur_interval.end
        return res
               

# third round

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        def cmp(interval1, interval2):
            if interval1.start == interval2.start:
                return interval1.end - interval2.end
            return interval1.start - interval2.start
            
        intervals.sort(cmp)
        res = []
        for interval in intervals:
            if not res:
                res.append(interval)
            else:
                if res[-1].end >= interval.start:
                    res[-1].end = max(interval.end, res[-1].end)
                else:
                    res.append(interval)
        return res
        
