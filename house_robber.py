class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        # record value and index
        # there should be only one able to be used
        largest = {}
        second_largest = {}
        index = 0 if nums[0]> nums[1] else 1
        largest[index] = nums[index]
        second_index = 0 if nums[0] < nums[1] else 1
        second_largest[second_index] = nums[second_index]
        for i in range(2, len(nums)):
            if largest.has_key(i-1):
                tmp = second_largest.values()
                if tmp[0] + nums[i] > largest.get(i-1):
                    #update largest and second_largest
                    tmpdict = largest.copy()
                    largest.clear()
                    largest[i] = tmp[0] + nums[i]
                    second_largest = tmpdict
            else:
                tmp = largest.values()
                tmpdict = largest.copy()
                largest.clear()
                largest[i] = tmp[0] + nums[i]
                second_largest = tmpdict
        maximum = largest.values()
        return maximum[0]
