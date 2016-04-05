class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        # the core idea is compare the single digit
        # idea is how to sort
        def cmp(num1, num2):
            s1 = str(num1)
            s2 = str(num2)
            r1, r2 = s1 + s2, s2 + s1
            if r1 > r2:
                return -1
            elif r1 < r2:
                return 1
            else:
                return 0
        nums.sort(cmp)
        res = ''
        # special case check for 0
        allZero = True
        for i, n in enumerate(nums):
            if n != 0:
                allZero = False
            if not allZero and i != len(nums)-1:
                res += str(n)
            if i == len(nums)-1:
                res += str(n)
        return res
