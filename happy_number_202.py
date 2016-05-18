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


#second round
class Solution2(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = set()
        # once we find a cycle, check whether the cycle entry point is 1
        while n not in nums:
            nums.add(n)
            n = self.get_square_num(n)
        if n == 1:
            return True
        else:
            return False
            
    def get_square_num(self, n):
        res = 0
        while n > 0:
            res += (n % 10) ** 2
            n /= 10
        return res
