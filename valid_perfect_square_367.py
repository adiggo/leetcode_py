class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # use binary search to get a number
        # validate whethere this number ** 2 == num
        if num < 0:
            return False
        s = self.get_square(0, num, num)
        return s ** 2 == num
        
        
    def get_square(self, left, right, num):
        while left <= right:
            mid = left + (right - left)/2 
            if mid ** 2 < num:
                left = mid + 1
            elif mid ** 2 > num:
                right = mid - 1
            else:
                return mid
        return left

        
        
        
