class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l1, l2 = len(a), len(b)
        carry = 0
        r = ''
        for i in range(max(l1, l2)):
            c1 = int(a[l1-1-i]) if l1-1-i < l1 and l1 -1 -i >= 0 else 0
            c2 = int(b[l2-1-i]) if l2-1-i < l2 and l2 -1 -i >= 0 else 0
            num = c1 ^ c2 ^ carry
            tmp = c1 + c2 + carry 
            if tmp > 1:
                carry = 1
            else:
                carry = 0
            r += str(num)
        if carry == 1:
            r += str(carry) 
        return r[::-1]
