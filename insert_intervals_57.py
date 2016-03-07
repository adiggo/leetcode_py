class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []
        if not intervals:
            return [newInterval]
        flag = False
        for i in range(len(intervals)):
            interval = intervals[i]
            if interval.start >= newInterval.start:
                if interval.start == newInterval.start:
                    res.append(Interval(newInterval.start, max(interval.end, newInterval.end)))
                    continue
                if interval.start > newInterval.end:
                    if not flag:
                        if i > 0 and intervals[i-1].end < newInterval.start:
                            res.append(newInterval)
                        flag = True
                    res.append(interval)
                else:
                    if i > 0 and intervals[i-1].end >= newInterval.start:
                        res[-1].end = max(interval.end, newInterval.end)
                    else:
                        res.append(Interval(newInterval.start, max(interval.end, newInterval.end)))
            else:
                if interval.end >= newInterval.start:
                    res.append(Interval(interval.start, max(interval.end, newInterval.end)))
                else:
                    res.append(interval)
        if intervals[0].start > newInterval.end:
            res.insert(0, newInterval)
        if intervals[len(intervals)-1].end < newInterval.start:
            res.append(newInterval)
        return res
