class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        # running time should be O(n * k^2) --> k is the average length of word in the words list
        # since words are unique. we can map a unique word to its index.
        word_map = {y: x for x, y in enumerate(words)}

        def isPalindrome(word):
            size = len(word)
            for x in range(size / 2):
                if word[x] != word[size - x - 1]:
                    return False
            return True

        res = set()
        # the assumption is that single word length should be much smaller than the amount of words
        for index, word in enumerate(words):
            # 1. if the word is palindrome, check whether our map contains ""
            # 2. check whether map contains the reversed word  
            # 3. check left/right word
            if "" in word_map and word != "" and isPalindrome(word):
                bidx = word_map[""]
                res.add((bidx, index))
                res.add((index, bidx))

            reverse_word = word[::-1]

            if reverse_word in word_map:
                reverse_index = word_map[reverse_word]
                if index != reverse_index:
                    res.add((index, reverse_index))
                    res.add((reverse_index, index))

            for x in range(1, len(word)):
                left, right = word[:x], word[x:]
                reverse_left, reverse_right = left[::-1], right[::-1]
                if isPalindrome(left) and reverse_right in word_map:
                    res.add((word_map[reverse_right], index))
                if isPalindrome(right) and reverse_left in word_map:
                    res.add((index, word_map[reverse_left]))
        return list(res)
