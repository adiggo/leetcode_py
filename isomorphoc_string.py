class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if s is None or t is None:
            return False
        if len(s) != len(t):
            return False
        
        helper = {}
        for i in range(len(s)):
            if s[i] in helper:
                if helper.get(s[i]) != t[i]:
                    return False
                else:
                    continue
            else:
                helper[s[i]] = t[i]
        helper.clear()
        for i in range(len(s)):
            if t[i] in helper:
                if helper.get(t[i]) != s[i]:
                    return False
                else:
                    continue
            else:
                helper[t[i]] = s[i]
        return True
