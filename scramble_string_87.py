class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # pre- check
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if not self.checkChar(s1, s2):
            return False
        # they met the basic condition to be scramble string
        # the divide point should be the point where they have 
        # so use the util method to find the cut point
        d = dict()
        for i in xrange(1, len(s1)):
            if self.isScramble(s1[i:], s2[i:]) and self.isScramble(s1[:i], s2[:i]):
                return True
            else:
                if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                    return True
        return False
                    
    def checkChar(self, s1, s2):
        d = dict()
        for c in s1:
            d[c] = d.get(c, 0) + 1
        for c in s2:
            if c not in d:
                return False
            else:
                d[c] = d.get(c)-1
                if d[c] < 0:
                    return False
        return True
