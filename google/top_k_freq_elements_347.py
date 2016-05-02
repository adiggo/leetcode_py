
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = dict()
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        heap = []
        size = len(freq)
        res = []
        for i, n in enumerate(freq):
            f = freq[n]
            heapq.heappush(heap, (-f, n))
            if i >= (size - k):
                res.append(heapq.heappop(heap)[1])
        return res
