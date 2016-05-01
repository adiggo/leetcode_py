class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # no duplicate numbers
        fac = [1]
        for i in range(1, n):
            fac.append(fac[-1] * i)
        res = []
        nums = range(1, n+1)
        for i in xrange(n):
            digit = (k-1) / fac[n-i-1]
            res.append(str(nums[digit]))
            nums.remove(nums[digit])
            k = k % fac[n-i-1]
        return ''.join(res)

