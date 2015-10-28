class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.minheap, self.maxheap = [], []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if self.size % 2 == 0:
            if len(self.minheap) == 0:
                heapq.heappush(self.maxheap, -1 * num)
            else:
                toMax = -1 * heapq.heappushpop(self.minheap, num)
                heapq.heappush(self.maxheap, toMax)
            self.size += 1
        else:
            toMin = -1 * heapq.heappushpop(self.maxheap, -1 * num)
            heapq.heappush(self.minheap, toMin)
            self.size += 1        
    
    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.size == 0:
            return 0.0
        if self.size % 2 == 1:
            return (float)(-1 *self.maxheap[0])
        else:
            return (-1* self.maxheap[0] + self.minheap[0])/2.0
