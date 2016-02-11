class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # the max num is x/2
        # binary search
        if x == 0:
            return 0
        start = 0
        end = x
        while start <= end:
            mid = start + (end - start)/2
            if mid * mid > x:
                end = mid - 1
            elif mid * mid < x:
                start = mid+1
            else:
                return mid
        return start-1
