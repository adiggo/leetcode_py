# O(n) running time
# Manacher's Algorith

class Solution(object):
    def longestPalindrome(self, s):
        if s is None or s == '':
            return ''
        new_s = self.getNewInput(s)
        C, R = 0, 0
        P = [1] * len(new_s)
        for i in range(1, len(new_s)-1):
            mirror_i = 2*C - i
            P[i] = min(P[mirror_i], R-i) if R > i else 0
            while new_s[i + P[i] + 1] == new_s[i - P[i]-1]:
                P[i] += 1
            if P[i] + i > R:
                C = i
                R = i + P[i]
        maxLen, center = 0, 0
        for i in range(1, len(new_s)-1):
            l = P[i]
            if l > maxLen:
                maxLen = l
                center = i

        return s[(center-maxLen-1)/2:(center-maxLen-1)/2+maxLen]

    def getNewInput(self, s):
        res = '*#'
        for c in s:
           res += c
           res += '#'
        res += '&'
        return res
