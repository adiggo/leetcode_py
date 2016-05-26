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
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_map = dict()
        visited_str = set()
        # optimize this later
        words = str.split()
        l = len(pattern)
        if l != len(words):
            return False
        else:
            for i in xrange(l):
                c = pattern[i]
                word = words[i]
                if c in str_map:
                    if str_map[c] != word:
                        return False
                else:
                    if word in visited_str:
                        return False
                    str_map[c] = word
                    visited_str.add(word)
        return True
            
