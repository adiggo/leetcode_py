#similar to ugly number 2
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        indexes = [0] * len(primes)
        ugly_nums = [1]
        while len(ugly_nums) < n:
            l = []
            for i in xrange(len(primes)):
                l.append(ugly_nums[indexes[i]] * primes[i])
            m = min(l)
            for i in xrange(len(l)):
                if l[i] == m:
                    indexes[i] += 1
            ugly_nums += m,
        return ugly_nums[-1]
