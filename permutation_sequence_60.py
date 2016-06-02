class Solution(object):
    # we can use linkedlist to reduce complexity due to the remove in the for loop
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # no duplicate numbers
        fac = [1]
        for i in xrange(1, n):
            fac.append(fac[-1] * i)
        res = []
        nums = range(1, n+1)
        for i in xrange(n):
            index = (k-1) / fac[-i-1]
            res.append(str(nums[index]))
            nums.remove(nums[index])
            k = k % fac[-i-1]
        return ''.join(res)
