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
