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




