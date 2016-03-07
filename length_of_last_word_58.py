class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        if not s:
            return res
        flag = False
        for i in range(len(s)-1, -1, -1):
            if flag and s[i] == ' ':
                break
            # set flag to true if meet a charater is not empty
            if s[i] != ' ':
                flag = True
                res += 1
        return res
