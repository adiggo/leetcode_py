class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        sorted_nums = sorted(nums)
        # put the first half in even index, put the second half in odd index
        for x in range(1, size, 2) + range(0, size, 2):
            nums[x] = sorted_nums.pop()
