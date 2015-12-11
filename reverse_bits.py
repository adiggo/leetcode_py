class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # use an additional var current index
        if n is None:
            return 0
        res = 0
        cur_index = 31
        for i in range(32):
            res <<= 1
            if n & 1 == 1:
                res += 1
            cur_index, n = cur_index - 1, n >> 1
        return res
