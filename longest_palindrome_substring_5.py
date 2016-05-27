class Solution(object):
    
    def longestPalindrome(self, s):
        if s is None or s == '':
            return ''
        if len(s) == 1:
            return s
        longest = s[0]
        for i in xrange(len(s)):
            tmp = self.helper(s, i, i)
            if len(tmp) > len(longest):
                longest = tmp
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(longest):
                longest = tmp
        return longest

    def helper(self, s, begin, end):
        while begin >=0 and end < len(s) and s[begin] == s[end]:
            begin -= 1
            end += 1
        return s[begin+1: end]

