class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        helper = [0] * (len(s)+1)
        # no way to resolve a decoded string starting from 0
        if self.checkSingleDigit(s[0]):
            helper[0] = 1
        else:
            return 0
        if len(s) > 1:
            num = self.checkDoubleDigits(s[0], s[1])
            helper[1] = num
            if num == 0:
                return 0
    
        for i, c in enumerate(s):
            if i == 0 or i == 1:
                continue
            helper[i] += helper[i-1]* self.checkSingleDigit(s[i])
            if s[i-1] == '1' or s[i-1] == '2':
                if int(s[i-1: i+1]) >= 10 and int(s[i-1:i+1]) <= 26:
                    helper[i] += helper[i-2] 
            if helper[i] == 0:
                return 0
        return helper[len(s)-1]
            
    #return 0 or 1
    def checkSingleDigit(self, c):
        if ord(c) - ord('0') > 0 and ord(c) - ord('0') <10:
            return 1
        else:
            return 0
    # return 0, 1 or 2
    def checkDoubleDigits(self, c1, c2):
        if not self.checkSingleDigit(c1):
            return 0
        else:
            if c2 == '0':
                if c1 == '1' or c1 == '2':
                    return 1
                else:
                    return 0
            elif ord(c2) - ord('0') > 0 and ord(c2) - ord('0') < 10:
                if c1 == '1':
                    return 2
                elif c1 == '2':
                    if ord(c2) -  ord('0') > 0 and ord(c2) <= ord('6'):
                        return 2
                    else:
                        return 1
                else:
                    return 1
