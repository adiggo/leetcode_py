class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maj = nums[0]
        for num in nums:
            if maj == num:
                count += 1
                if count > len(nums)/2:
                    return maj
            else:
                count -= 1
                if count == 0:
                    maj = num
                    count = 1
        return maj
