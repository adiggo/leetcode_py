class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        longest_prefix = strs[0]
        for i in xrange(1, len(strs)):
            minL = min(len(strs[i]), len(longest_prefix))
            flag = False
            for j in xrange(min(len(strs[i]), len(longest_prefix))):
                if strs[i][j] != longest_prefix[j]:
                    longest_prefix = longest_prefix[:j]
                    flag = True
                    break
            if not flag and len(longest_prefix) >len(strs[i]):
                longest_prefix = longest_prefix[:minL]
        return longest_prefix
