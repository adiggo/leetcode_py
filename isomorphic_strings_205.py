class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(pattern) != len(words):
            return False
        pattern_map = dict()
        words_set = set()
        for i in xrange(len(pattern)):
            if pattern[i] in pattern_map:
                if words[i] != pattern_map.get(pattern[i]):
                    return False
            else:
                if words[i] in words_set:
                    return False
                else:
                    words_set.add(words[i])
                    pattern_map[pattern[i]] = words[i]
        return True

# second round
class Solution2(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        pattern = dict()
        t_set = set()
        for i in xrange(len(s)):
            if s[i] not in pattern:
                # foo  --> bar   
                if t[i] in t_set:
                    return False
                else:
                    pattern[s[i]] = t[i]
                    t_set.add(t[i])
            else:
                if t[i] != pattern.get(s[i]):
                    return False
        return True
