#reference: http://bookshadow.com/weblog/2015/08/19/leetcode-ugly-number-ii/
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # inital value is 1
        ugly_nums= [1]
        i2 = i3 = i5 = 0
        while len(ugly_nums) < n:
            m2, m3, m5 = ugly_nums[i2] * 2, ugly_nums[i3] * 3, ugly_nums[i5] * 5
            m = min(m2, m3, m5)
            # 2 have priority, then 3, then 5
            if m == m2:
                i2 += 1
            if m == m3:
                i3 += 1
            if m == m5:
                i5 += 1
            ugly_nums += m,
        return ugly_nums[-1]
