class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n == 1 or n == 2:
            return True
            
        if n % 2==1 or n <= 0:
            return False
            
        while n >2:
            n = n>>1
            if n % 2 ==1:
                return False
        return True

    # better approach. since if n is pow(2), then its right digit should be zero except one. so n & (n-1) should be zero
    def isPowerOfTwo2(self, n):
        return (n > 0) and (not n & (n - 1))
        
