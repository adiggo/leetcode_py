class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        res = []
        for i in range(len(digits)-1, -1, -1):
            num = 1 + digits[i] + carry if i == len(digits) -1 else digits[i] + carry
            carry = num / 10 
            res.append(num % 10)
        if carry > 0:
            res.append(carry)
        res.reverse()
        return res
            
            
