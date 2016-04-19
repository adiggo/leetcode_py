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
