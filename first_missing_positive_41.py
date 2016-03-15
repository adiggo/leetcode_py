class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        l = len(nums)
        i = 0
        while i < l:
            v = nums[i]
            if v <= 0 or v > l or v == i+1:
                i += 1
                continue
            else:
                if nums[i] == nums[v-1]:
                    i += 1
                    continue
                nums[i], nums[v-1] = nums[v-1], v
                    
        for i in range(l):
            if nums[i] != i+1:
                return i+1
        return nums[-1]+1
