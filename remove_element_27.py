class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # length of the element 
        length = len(nums)
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                length -= 1
                nums[length], nums[i]= nums[i], nums[length]
        return length
