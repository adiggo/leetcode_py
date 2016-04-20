class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # min heap
        self.h1 = []
        # max heap
        self.h2 = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.h1) == 0:
            self.h1.append(num)
        elif len(self.h1) == 1 and len(self.h2) == 0:
            if num > self.h1[0]:
                prev = self.h1.pop()
                self.h2.append(-prev)
                self.h1.append(num)
            else:
                self.h2.append(-num)
        else:
            if -num > self.h2[0]:
                heapq.heappush(self.h2, -num)
            else:
                heapq.heappush(self.h1, num)
            # balance
            if len(self.h1) > len(self.h2):
                heapq.heappush(self.h2, -heapq.heappop(self.h1))
            elif len(self.h1) < len(self.h2):
                heapq.heappush(self.h1, -heapq.heappop(self.h2))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if not self.h1 and not self.h2:
            return 0
        l1, l2 = len(self.h1), len(self.h2)
        if l1 == l2:
            return float(self.h1[0] - self.h2[0]) / 2
        else:
            return float(self.h1[0]) if l1 > l2 else -float(self.h2[0])


# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
