class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        #num1 & num2
        if num1 == '0' or num2 == '0':
            return '0'
        res = ''
        helper = []
        pos = 0
        carry = 0
        for i in reversed(num2):
            carry = 0
            index = 0
            for j in reversed(num1):
                m = int(j) * int(i) + carry
                carry = m / 10
                m = m % 10
                if len(helper) <= pos+index:
                    helper.append(m)
                else:
                    new_val = helper[pos+index] + m 
                    helper[pos+index] = new_val % 10
                    carry += new_val / 10
                index += 1
            pos += 1
            if carry != 0:
                helper.append(carry)
        res = ''.join(str(e) for e in helper)
        return res[::-1]
