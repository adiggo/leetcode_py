class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        # 2 * 5 has 0.
        # calculate how many 5 u have
        res = 0
        while n != 0:
            res += n / 5 
            n = n/5
        return res
        
