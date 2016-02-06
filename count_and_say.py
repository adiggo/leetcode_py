class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1:
            return None
        res = '1'
        i = 1
        while i < n:
            res = self.count(res)
            i+=1
        return res
            
            
    def count(self, num):
        c = 1
        prev = num[0]
        res = ''
        for i in num[1:]:
            if i == prev:
                c += 1 
            else:
                res += str(c)
                res += prev
                c = 1
                prev = i
        res += str(c) + prev
        return res
