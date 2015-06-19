class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        # get all digit
        if n <= 0:
            return False
        helper = set()
        while n!= 1:
            if n in helper:
                return False
            helper.add(n)
            digits = []
            while n > 0:
                digits.append(n % 10)
                n = n/10
            sum = 0
            for digit in digits:
                sum += int(math.pow(digit, 2))
            n = sum
        return True
