class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        steps = [0] * len(nums)
        max_reach = 0
        for i, num in enumerate(nums):
            for j in range(max_reach+1, min(len(nums), i+num+1)):
                if steps[j] > steps[i] + 1 or steps[j] == 0:
                    steps[j] = steps[i] + 1
            max_reach = max(max_reach, i+num)
            if max_reach >= len(nums)-1:
                break
        return steps[-1]



