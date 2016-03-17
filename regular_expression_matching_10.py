
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        l1, l2 = len(s), len(p)
        for i in range(min(l1, l2)):
            if s[i] == p[i]:
                continue
            else:
                # single character match
                if p[i] == '.':
                    continue
                elif p[i] == '*':
                    for j in range(l1-i):
                        if self.isMatch(p[i+1:], s[i+j:]):
                            return True
                        else:
                            continue
                else:
                    continue
        return True if l1 == l2 else False
        
