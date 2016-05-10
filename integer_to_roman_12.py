class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500 ,'M': 1000, 'IV': 4, 'IX': 9, 'XL':40, 'XC':90, 'CD':400, 'CM': 900}
        digits = {v: k for k, v in roman.items()}
        # for integer 4 and 9, need to deal 
        # from high to low
        carry = 0
        res = []
        while num > 0:
            r = num / 10
            m = num % 10
            cur = 10 **carry
            if m * cur in digits:
                # IV, IX, XL ....
                res.append(digits.get(m * cur))
            else:
                if m > 5:
                    res.append((m-5)*digits.get(cur))
                    res.append(digits.get(5 * cur))
                else:
                    res.append(m*digits.get(cur))
            carry += 1
            num = num/10
        return ''.join(res[::-1])


# a better approach: start from 1000 to 1, each time get the division value.
class Solution2(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        syms = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        # start from high digits        
        res = ''
        i = 0
        while num > 0:
            d = num / nums[i]
            res += d * syms[i]
            num -= d * nums[i]
            i += 1
        return res
