class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 2 if n == 2 else 1 if n == 1 else 0
        prev = 1
        cur = 2
        res = 0
        for i in range(3,n):
            tmp = cur
            cur = cur+prev
            prev = tmp
        res = prev + cur
        return res
        

    def climbStairs2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1 or n == 2:
            return n
        l = [-1] * n
        self.dfs(n, l)
        return l[-1]
        
    def dfs(self, n, l):
        if n <= 0:
            return
        if n == 1 or n == 2:
            l[n-1] = n
            return
        if l[n-2] == -1:
            self.dfs(n-1, l)
        if l[n-3] == -1:
            self.dfs(n-2, l)
        l[n-1] = l[n-2] + l[n-3] 
