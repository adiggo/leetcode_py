class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        if not nums:
            return 0
        heap = []
        for n in nums:
            heapq.heappush(heap, -n)
        res = 0
        for i in xrange(k):
            if i == k-1:
                return -heapq.heappop(heap)
            heapq.heappop(heap)
