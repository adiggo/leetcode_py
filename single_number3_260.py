class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # use xor
        xor_v = reduce(lambda x,y: x^y, nums)
        low_bits = xor_v & -xor_v
        s1, s2 = 0, 0
        for n in nums:
            if n & low_bits:
                s1 ^= n
            else:
                s2 ^= n
        return [s1, s2]
