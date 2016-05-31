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

# second round
class Solution2(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # the max number for sqrt is x/2 + 1
        if x < 0:
            raise Exception('input should be larger than zero')
            
        l, r = 0, x/2 + 1
        while l <= r:
            mid = l + (r - l)/2
            tmp = mid ** 2
            if tmp > x:
                r = mid - 1
            elif tmp < x:
                l = mid + 1
            else:
                return mid
        return l - 1

# babylonian method
def square_root(n):
    '''
    @param n: float number
    @return: float number
    '''
    x = n
    y = 1.0
    e = 0.01
    while abs(x - y) > e:
        x = (x + y) / 2
        y = n / x
    return x


# make a guess
# divide original number by the guess number
# average of these number
# use this average as next result

print square_root(5.0)

