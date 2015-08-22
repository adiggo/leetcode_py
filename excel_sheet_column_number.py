class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if s is None or len(s) == 0:
            return 0
        length = len(s)
        res = 0
        for i in range(length):
            current_char = s[i]
            res += (ord(current_char) - ord('A') + 1)* math.pow(26, length-i-1)
        
        return int(res)
