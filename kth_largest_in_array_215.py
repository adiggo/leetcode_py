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

# quick sort
class Solution2:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        return self.quickSort(nums, len(nums)-k, 0, len(nums)-1)
        
    def quickSort(self, nums, k, start, end):
        if start >= end:
            return nums[start]
        pIndex = self.partition(nums, start, end)
        if pIndex == k:
            return nums[pIndex]
        elif pIndex < k:
            return self.quickSort(nums, k, pIndex+1, end)
        else:
            return self.quickSort(nums, k, start, pIndex -1)
        
    # return the sorted Index
    def partition(self, nums, start, end):
        p = nums[start]
        pIndex = start
        localIndex = pIndex + 1
        while localIndex <= end:
            if nums[localIndex] < p:
                #swap
                pIndex += 1
                nums[pIndex], nums[localIndex] = nums[localIndex], nums[pIndex]
            localIndex += 1
        nums[start], nums[pIndex] = nums[pIndex], nums[start]
        return pIndex
