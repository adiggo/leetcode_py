class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        # this is how we define prime
        # PRIME integer is the positive integer must be larger than 1
        # two step:
        # whether a number is prime
        # coutn how many less than n
        if n <= 1:
            return 0
        count = 0
        helper = [True]*n
        for i in range(2, int(math.ceil(math.sqrt(n-1)))+1):
            if helper[i]:
                j = 2*i
                while j < n:
                    #set this index as False
                    helper[j] = False
                    j += i

        for i in range(2, n):
            if helper[i]:
                count += 1
        return count


# reference: http://bookshadow.com/weblog/2015/04/27/leetcode-count-primes/
# implement sieve of Erotosthenes
class Solution2:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        # handle special case when n < 2
        isPrime = [True] * max(n, 2)
        isPrime[0], isPrime[1] = False, False
        # initial value as 2, implement sieve of Eratosthenes
        x = 2
        while x * x < n:
            # filter out numbers that already is not prime due to previou check
            if isPrime[x]:
                p = x * x
                while p < n:
                    isPrime[p] = False
                    p += x
            x += 1
        return sum(isPrime)
