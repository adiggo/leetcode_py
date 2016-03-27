class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i, j = 1, 1
        while i < len(nums):
            z = i
            while i < len(nums) and nums[i] == nums[i-1]:
                nums[j] = nums[i]
                i += 1
                if i - z > 1:
                    continue
                j += 1
            if i == len(nums):
                break
            nums[j] = nums[i] 
            i, j = i+1, j+1
        return j
