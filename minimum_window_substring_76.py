class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ''
        start, end = 0, 0
        helper = dict()
        i = 0
        l = len(s)
        res = l
        tMapper = self.getCharFreq(t)
        minS = ''
        for i in xrange(l):
            end = i
            helper[s[i]] = helper.get(s[i], 0) + 1
            if self.checkContains(helper, tMapper):
                while start <= end:
                    helper[s[start]] -= 1
                    if s[start] in tMapper and helper[s[start]] < tMapper[s[start]]:
                        start += 1
                        break
                    start += 1
                if end-start+2 <= res:
                    minS = s[start-1:end+1]
                    res = end - start + 2
        return minS
                    
                
    def getCharFreq(self, t):
        helper = dict()
        for c in t:
            if c in helper:
                helper[c] += 1
            else:
                helper[c] =1 
        return helper
                
    
    def checkContains(self, s, t):
        for i in t:
            if i in s and s[i] >= t[i]:
                continue
            else:
                return False
        return True
