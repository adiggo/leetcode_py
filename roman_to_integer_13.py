# second round
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500 ,'M': 1000, 'IV': 4, 'IX': 9, 'XL':40, 'XC':90, 'CD':400, 'CM': 900}
        # IV, IX, XL, XC, CD, CM
        # 999 CMXCIX
        i = 0
        res = 0
        while i < len(s):
            c = s[i]
            next = s[i+1] if i+1 < len(s) else ''
            if c + next in roman:
                res += roman.get(c+next)
                i += 2
            else:
                res += roman.get(c)
                i += 1
        return res
                
