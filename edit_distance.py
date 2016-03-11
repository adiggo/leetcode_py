class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 is None or word2 is None:
            return abs(len(word1) if word1 else 0 - len(word2) if word2 else 0)
        arr = [[0 for i in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        #initialization
        
        for i in range(len(word1)):
            arr[i+1][0] = i+1
        for j in range(len(word2)):
            arr[0][j+1] = j+1
        
        for i, c1 in enumerate(word1):
            for j, c2 in enumerate(word2):
                if c1 == c2:
                    arr[i+1][j+1] = arr[i][j]
                else:
                    arr[i+1][j+1] = 1 + min(arr[i][j+1], arr[i+1][j], arr[i][j])
        return arr[len(word1)][len(word2)]




# recursive method. but have too much duplicated calculation
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 is None or word2 is None:
            return abs(len(word1) if word1 else 0 - len(word2) if word2 else 0)
        for i in range(min(len(word1), len(word2))):
            if word1[i] == word2[i]:
                continue
            else:
                #insert
                r1 = self.minDistance(word1[i:], word2[i+1:])
                #delete
                r2 = self.minDistance(word1[i+1:], word2[i:])
                #update
                r3 = self.minDistance(word1[i+1:], word2[i+1:])
            return min(r1, r2, r3)
        return abs(len(word1) - len(word2))
