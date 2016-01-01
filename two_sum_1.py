class Solution(object):
    # two time scan
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        remainers = {}
        result = []
        for i in range(len(nums)):
            remainer = target - nums[i]
            #considering that there is only one remainer fits
            remainers[remainer] = i
        
        for i in range(len(nums)):
            if nums[i] in remainers:
                #make sure it is not the same number
                if i != remainers[nums[i]]:
                    result.append(i+1)
                    result.append(remainers[nums[i]]+1)
                    break
                else:
                    continue
        return result
    # only need one time scan
    def twoSum2(self, nums, target):
        helper = {}
        for i, v in enumerate(nums):
            if target - v in helper:
                return [helper[target-v]+1, i + 1]
            helper[i] = v
