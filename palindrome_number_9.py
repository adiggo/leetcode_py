class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #find length
        if x < 0:
            return False
        y = x
        length = 0
        while y > 0:
            length += 1
            y = y / 10 
        for i in range(1, length):
            if x <= 0:
                break;
            if x % 10 != x / pow(10,length-1):
                return False
            x = x % pow(10, length-1)
            x = x / pow(10, 1)
            length = length - 2
        return True
