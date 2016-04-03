class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        helper = set()
        helper.add(n)
        s = n
        
        def getDigitsSquareSum(num):
            res = 0
            while num > 0:
                res += (num % 10) ** 2
                num /= 10
            return res
            
        while True:
            s = getDigitsSquareSum(s)
            if s in helper and s != 1:
                return False
            if s == 1:
                return True
            if s not in helper:
                helper.add(s)
        return False
