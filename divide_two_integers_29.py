class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        res, sum = 0, 0
        a,b = dividend, divisor
        divisor, dividend = abs(divisor), abs(dividend)
        ds = []
        ds.append(divisor)
        while True:
            if sum + ds[-1] > dividend:
                break
            else:
                sum += ds[-1]
                res = 2 * res if res != 0 else 1
                if res != 1:
                    ds.append(sum)
                else:
                    continue
        has_negative = True if (a < 0 and b > 0) or (a > 0 and b < 0) else False
        for i in range(len(ds)-2, -1, -1):
            if sum + ds[i] > dividend:
                continue
            else:
                sum += ds[i]
                res += pow(2, i)
        if not has_negative:
            return min(res, pow(2, 31)-1)
        else:
            return -res
