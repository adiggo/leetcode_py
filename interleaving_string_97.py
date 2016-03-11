class Solution(object):
    # recursive method
    # there are some duplication calculation
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # similar to edit distance
        if len(s1) + len(s2) != len(s3):
            return False
        i1, i2 = 0, 0
        return self.dfs(s1, s2, s3, 0, 0, 0)

    def dfs(self, s1, s2, s3, i1, i2, i3):
        if i3 == len(s3):
            return True
        c1 = s1[i1] if i1 < len(s1) else None
        c2 = s2[i2] if i2 < len(s2) else None
        if c1 == c2:
            if s3[i3] != c1:
                return False
            else:
                if c1 and c2:
                    return self.dfs(s1, s2, s3, i1 + 1, i2, i3 + 1) or self.dfs(s1, s2, s3, i1, i2 + 1, i3 + 1)
                elif c1:
                    return self.dfs(s1, s2, s3, i1 + 1, i2, i3 + 1)
                elif c2:
                    return self.dfs(s1, s2, s3, i1, i2 + 1, i3 + 1)
        else:
            if s3[i3] != c1 and s3[i3] != c2:
                return False
            elif s3[i3] == c1:
                return self.dfs(s1, s2, s3, i1 + 1, i2, i3 + 1)
            else:
                return self.dfs(s1, s2, s3, i1, i2+1, i3 + 1)


    def dpIsInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # similar to edit distance
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        # initialization
        dp = [[False for i in range(l2+1)] for i in range(l1+1)] 
        dp[0][0] = True
        for i in range(l1):
            dp[i+1][0] = dp[i][0] if s1[i] == s3[i] else False
        for j in range(l2):
            dp[0][j+1] = dp[0][j] if s2[j] == s3[j] else False
        # transfer function
        for i in range(l1+1):
            for j in range(l2+1):
                if i== 0 or j==0: continue
                if s1[i-1] == s3[i+j-1] and dp[i-1][j]:
                    dp[i][j] = True
                if s2[j-1] == s3[i+j-1] and dp[i][j-1]:
                    dp[i][j] = True
        return dp[l1][l2]
