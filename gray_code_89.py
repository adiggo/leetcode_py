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


# better approach. 0, 1 --> 0, 1, 11(3), 10(2)--> so we don't need to pre-append '0' since it will not change the final result 
class Solution2(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(n):
            for j in range(len(res)-1, -1, -1):
                res.append(res[j] + (1 << i))
        return res

# second round
# reverse the list each iteration: pattern searching
class Solution2(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        cur = [0, 1]
        for i in xrange(2, n+1):
            appender = (1 << (i-1))
            for j in reversed(cur):
                cur.append(appender + j)
        return cur if n >= 1 else [0]
