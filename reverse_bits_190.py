class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = 0
        for i in xrange(32):
            b = n & 1
            r |= b
            if i == 31:
                break
            r <<= 1
            n >>= 1
        return r
        


# reference:https://leetcode.com/discuss/27338/8ms-c-code-some-ideas-about-optimization-spoiler 
class Solution2(object):
    def __init__(self):
        self.mapper = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
    
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        msk = 0xF
        for i in xrange(8):
            res <<= 4
            res |= self.mapper[msk & n]
            n >>= 4
        return res
