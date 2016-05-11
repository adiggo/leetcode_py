class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            count = 0
            for num in nums:
                if num >> i & 1:
                    count += 1
            if count % 3 and i != 31:
                res += 1 << i
            if count % 3 and i == 31:
                # res currently is 2's complement, -10000000000 --> the lower bits will be setting to 1, other ones will be setting to zero. Then mark it as negative
                res -= 1 << 31
        return res

