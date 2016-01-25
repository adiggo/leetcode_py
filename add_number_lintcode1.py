class Solution:
    """
    @param a: The first integer
    @param b: The second integer
    @return:  The sum of a and b
    """
    def aplusb(self, a, b):
        # write your code here, try to do it without arithmetic operators.
        i = 0
        carry = 0
        res = 0
        for i in range(32):
            a_bit = a & 1
            b_bit = b & 1
            sum_bit = a_bit ^ b_bit
            sum_bit ^= carry
            carry = 1 if (a_bit == 1 and b_bit == 1) or (a_bit | b_bit == 1 and carry == 1) else 0
            sum_bit = sum_bit << i
            # use or since sum_bit is a single digit ---> 10000000, and res's bit length is len(sum_bit) - 1
            res |= sum_bit
            a >>= 1
            b >>= 1
        return res
