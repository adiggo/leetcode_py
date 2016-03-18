class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = self.gray(n)
        r = []
        for i in res:
            r.append(int(i, 2))
        return r
    
    def gray(self, n):
        if n <= 0:
            return ['0']
        if n == 1:
            return ['0','1']
        res = self.gray(n-1)
        r = []
        for code in res:
            r.append('0'+ code)
        for code in reversed(res):
            r.append('1' + code)
        return r
