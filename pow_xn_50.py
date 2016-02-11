class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        negative = False
        if n < 0:
            negative = True
        if negative:
            return 1/self.recursion(x, abs(n))
        else:
            return self.recursion(x, n)
            
        
    def recursion(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        p = self.recursion(x,n/2)
        return float(p*p*x) if n%2 ==1 else float(p*p)
