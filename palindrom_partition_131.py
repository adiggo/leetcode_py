class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s, res, [])
        return res

    def dfs(self, s, res, cur):
        if not s:
            res.append(list(cur))
            return

        for j in xrange(len(s)):
            if self.isPalindrome(s[:j+1]):
                cur.append(s[:j + 1])
                self.dfs(s[j + 1:], res, cur)
                cur.pop()

    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while right > left:
            if s[left] == s[right]:
                right -= 1
                left += 1
            else:
                return False
        return True
            
