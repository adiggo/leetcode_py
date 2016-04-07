class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        # consider what is bitwise and
        # one characteristic is that 0 & * is 0
        res = 0
        i = 0
        while m > 0 and n > 0:
            d = 0
            if m != n:
                d = 0
            else:
                d = ((m & 1) & (n & 1))
            d <<= i
            res |= d
            m >>= 1
            n >>= 1
            i += 1
        return res

# optimized version
class Solution2:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        # consider what is bitwise and
        # one characteristic is that 0 & * is 0
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return m << i
            
