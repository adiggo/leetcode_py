class Solution:

    def convertToTitle(self, n):
        res = ''
        while n >= 1:
            remain = n % 26
            remain_str = self.convertNumToChar(remain)
            res = remain_str + res
            n = (n-1)/26
        return res
        
    def convertNumToChar(self, num):
        if num > 26 or num < 0:
            return None
        if num == 0 :
            return 'Z'
        return chr(ord('A') + num - 1)
