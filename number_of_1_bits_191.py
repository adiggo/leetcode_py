class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        count = 0
        for i in xrange(32):
            if n & 1:
                count += 1
            n >>= 1
        return count

