class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        major = nums[0]
        # appear time of major
        count = 1
        for i in nums[1:]:
            if i == major:
                count += 1
            else:
                count -= 1
                if count < 0:
                    count = 1
                    major = i
        
        #since there must be a major element
        return major
