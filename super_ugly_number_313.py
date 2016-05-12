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


# second round: 
# the main problem how to calculate the ugly numbers.
# we record the index of the ugly number for each prime number
# for dedup, it is necessary to increment the index for the corresponding prime if it equal to the min value.
class Solution2:
    # @param {int} n a positive integer
    # @param {int[]} primes the given prime list
    # @return {int} the nth super ugly number
    def nthSuperUglyNumber(self, n, primes):
        # Write your code here
        if n == 1:
            return 1
        ugly_nums = [1]
        indexes = [0] * len(primes)
        
        while len(ugly_nums) < n:
            min_v = None
            
            for i in xrange(len(indexes)):
                index = indexes[i]
                if not min_v or ugly_nums[index] * primes[i] < min_v[0]:
                    min_v = (ugly_nums[index] * primes[i], i)
                    

            for i in xrange(len(indexes)):
                index = indexes[i]    
                if ugly_nums[index] * primes[i] == min_v[0]:
                    indexes[i] += 1
                
            ugly_nums += min_v[0],
        return ugly_nums[-1]
