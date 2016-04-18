class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        #check each location
        if not secret or not guess:
            return ''
        a_num = 0
        digit_map1 = dict()
        digit_map2 = dict()
        for i in xrange(len(secret)):
            if secret[i] == guess[i]:
                a_num += 1
            else:
                digit_map1[secret[i]] = digit_map1.get(secret[i], 0) + 1
                digit_map2[guess[i]] = digit_map2.get(guess[i], 0) + 1
        res = str(a_num) + 'A' 
        b_num = 0
        for k in digit_map1:
            b_num += min(digit_map2.get(k, 0), digit_map1.get(k, 0))
        res = res + str(b_num) + 'B'
        return res



class Solution2(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        #check each location
        if not secret or not guess:
            return ''
        bull = 0
        result = [0] * 10
        cow = 0
        digit_map1 = dict()
        digit_map2 = dict()
        for i in xrange(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                if result[int(secret[i])] < 0:
                    cow += 1
                result[int(secret[i])] += 1
                if result[int(guess[i])] > 0:
                    cow += 1
                result[int(guess[i])] -= 1
        return str(bull)+ 'A' + str(cow) + 'B'
