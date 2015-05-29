class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        if k < 0 or n <=0:
            return [[]]
        
        res = []
        tmp = []
        self.com(k, n, 0 , tmp, res, 0)
        return res
    
    def com(self, k, n, index, tmp, res, cursum):
        if len(tmp) > k:
            return
        if cursum == n:
            if len(tmp) == k:
                component = list(tmp)
                res.append(component)
                return
        if cursum < n:
            for i in range(index+1,10):
                tmp.append(i)
                self.com(k, n, i, tmp, res, cursum + i)
                tmp.pop()
           
            
