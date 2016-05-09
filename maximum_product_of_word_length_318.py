# use a map to record char to words index set map information. indexes denote the possible word that does not have common char with current word
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res = 0
        char_mapper = {}
        for i, word in enumerate(words):
            indexes = set(range(i))
            for c in word:
                if c not in char_mapper:
                    char_mapper[c] = set()
                    char_mapper[c].add(i)
                else:
                    # avoid duplicated calculation
                    if i in char_mapper[c]:
                        continue
                    if indexes:
                        indexes = indexes - char_mapper[c]
                    char_mapper[c].add(i)
            max_len = 0
            for x in indexes:
                max_len = max(max_len, len(words[x]))
            res = max(len(word) * max_len, res)
        return res


# 2nd leetcode

class Solution2(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # the idea use indexes to record the indexes that does not have the chars current word have
        
        res = 0
        # map character to a set of words indexes that have the char
        char_word = dict()
        l = len(words)
        for i in xrange(l):
            word = words[i]
            index = set(range(i))
            for c in word:
                if c in char_word:
                    # duplicated char
                    if i in char_word[c]:
                        continue
                    char_word[c].add(i)
                    if index:
                        index = index - char_word[c]
                else:
                    char_word[c] = set()
                    char_word[c].add(i)
            maxLen = 0
            for j in index:
                maxLen = max(len(words[j]), maxLen)
            res = max(maxLen * len(word), res)
        return res


# bit manipulation
class Solution3(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        # since the char only has 26, use bit manipulation        
        res = 0
        l = len(words)
        elements = [0] * l
        for i in xrange(l):
            word = words[i]
            for c in word:
                elements[i] |= 1 << (ord(c)-ord('a'))
        
        for i in xrange(len(elements)):
            for j in xrange(i+1, len(elements)):
                if not (elements[i] & elements[j]):
                    res = max(len(words[i]) * len(words[j]), res)
        return res
