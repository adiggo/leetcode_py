class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        # convert to a model
        i = 0
        cur = n
        local_sum = 0
        lower_digits = 0
        prev = 0
        prev_base = 0
        exponent = 1
        while cur > 0:
            r = cur % 10
            lower_digits += 10**i*r
            if i == 0:
                local_sum += 1 if r >= 1 else 0
            else:
                base = self.__helper(i, prev_base, exponent)
                exponent = 10 * exponent
                prev_base = base
                if r > 0:
                    local_sum += (base-prev)
                    if r > 1:
                        local_sum += exponent + base
                        local_sum += (r - 2) * base
                        local_sum += prev
                    else:
                        local_sum += lower_digits - exponent + 1 + prev
            prev = local_sum
            cur = cur/10
            i += 1
        return local_sum
    
    def __helper(self, n, prev_base, exponent):
        if n == 1:
            return 1
        res = 0
        res += (exponent + prev_base)
        res += 9 * prev_base
        return res
