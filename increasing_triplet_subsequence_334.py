class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # record first, second
        if not nums or len(nums) < 3:
            return False
        first, second, newFirst = None, None, None
        flag = False
        for i in xrange(1, len(nums)):
            if nums[i-1] < nums[i] and not flag:
                flag = True
                first, second = nums[i-1], nums[i]
                continue
            if second is not None:
                if nums[i] > second:
                    return True
                else:
                    if newFirst is not None:
                        if nums[i] > newFirst:
                            first, second = newFirst, nums[i]
                        else:
                            newFirst = nums[i]
                    else:
                        if nums[i] > first:
                            second = nums[i] # update second
                        else:
                            newFirst = nums[i]
        return False
