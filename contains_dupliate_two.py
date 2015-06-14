class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        helper = {}
        # true if there is such two same element exist
        # false if no such two same element exist
        for i in range(len(nums)):
            if nums[i] in helper:
                prev_index = helper.get(nums[i])
                if i - prev_index <= k:
                    return True
                else:
                    # record its latest position
                    helper[nums[i]] = i
                    continue
            else:
                helper[nums[i]] = i
        
        return False
