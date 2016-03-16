class Solution(object):
    def isOneEdit(self, s1, s2):
        if s1 == None or s2 == None:
            return False
        l1, l2 = len(s1), len(s2)
        if abs(l1 - l2) > 1:
            return False
        if l1 > l2:
            return self.isOneEdit(s2, s1)
        if l1 == 0:
            return True
        num_ops = 0
        for i in range(min(l1, l2)):
            c1 = s1[i-1] if l1 != l2 else s1[i]
            if  num_ops == 0:
                if c1 != s2[i]:
                    num_ops += 1
            else:
                if c1 != s2[i]:
                    return False

        return True if num_ops == 0 or num_ops ==1 and s1[-1] == s2[-1] and l1 > 0  else False
            
s = Solution()
import sys

print s.isOneEdit(sys.argv[1], sys.argv[2])
