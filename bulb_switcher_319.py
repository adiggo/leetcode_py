# only need calculate the factor number of num is even or odd.
# most number's factor number (include 1 and itself) is even, except the number whose sqrt is int.

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))
