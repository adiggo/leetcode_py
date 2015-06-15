class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        # this is how we define prime
        # PRIME integer is the positive integer must be larger than 1
        # two step:
        # whether a number is prime
        # coutn how many less than n
        count = 0
        for i in range(2, n+1):
            r = int(math.ceil(math.sqrt(i)))
            if i == 2:
                count+=1
                continue
            if i ==3:
                count+=1
                continue
            if math.pow(r,2) == i:
                continue
            else:
                flag = False
                for j in range(2,r):
                    if i % j == 0:
                        flag = True
                        break
                    else:
                        continue
                if not flag:
                    count+=1
        return count
