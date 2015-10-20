class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        helper = str(x).strip()
        
        res = ''
        is_negative = False
        for i in helper:
            if i == '-':
                is_negative = True
            else:
                res = i + res
        if is_negative:
            res = '-' + res
        
        return int(res) if int(res) < math.pow(2, 31)-1 and int(res) > - math.pow(2, 31) + 1 else 0
