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
