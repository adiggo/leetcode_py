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

# second round
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # num1 & num2
        if not num1 or not num2:
            return None
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = [0] * (len(num1) + len(num2))
        for i, n1 in enumerate(num1):
            d1 = int(n1)
            carry = 0;
            for j, n2 in enumerate(num2):
                d2 = int(n2)
                cur = d2 * d1 + carry + res[i + j]
                r = cur % 10
                res[i + j] = r
                carry = cur / 10
            if carry != 0:
                res[i + len(num2)] = res[i + len(num2)] + carry
        end = len(num1) + len(num2) - 1
        while end >= 0 and res[end] == 0:
            end -= 1
        return ''.join([str(x) for x in res[::-1][len(res) - 1 - end:]]) if end >= 0 else '0'

    def multiply_optimization(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # num1 & num2
        if not num1 or not num2:
            return None
        res = [0] * (len(num1) + len(num2))
        for i in xrange(len(num1) - 1, -1, -1):
            carry = 0
            d1 = int(num1[i])
            for j in xrange(len(num2) - 1, -1, -1):
                d2 = int(num2[j])
                cur = d2 * d1 + carry + res[i + j + 1]
                r = cur % 10
                res[i + j + 1] = r
                carry = cur / 10
            if carry != 0:
                res[i] = res[i] + carry
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1
        return ''.join([str(x) for x in res[start:]]) if start < len(res) else '0'

