class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if nums is None or len(nums)< 4:
            return []
        sum_nums = {}
        nums.sort()
        res = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] not in sum_nums:
                    sum_nums[nums[i]+nums[j]] = [(i, j)]
                else:
                    sum_nums[nums[i]+nums[j]].append((i, j))
        for i in range(len(nums)):
            for j in range(i+1, len(nums)-2):
                num = target - nums[i] - nums[j]
                if num in sum_nums:
                    for index in sum_nums[num]:
                        if index[0] > j:
                            res.add((nums[i], nums[j], nums[index[0]], nums[index[1]]))
        return [list(ele) for ele in res]
        
