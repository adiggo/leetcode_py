class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        # bull number
        num_A = 0
        # cow number
        num_B = 0
        
        map_A = {}
        map_B = {}
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                num_A += 1
            else:
                if secret[i] in map_A:
                    map_A[secret[i]] = map_A.get(secret[i]) + 1
                else:
                    map_A[secret[i]] = 1
                if guess[i] in map_B:
                    map_B[guess[i]] = map_B.get(guess[i]) + 1
                else:
                    map_B[guess[i]] = 1
        for key in map_A:
            if map_B.get(key):
                num_B += min(map_A.get(key), map_B.get(key))
        return str(num_A) + 'A' + str(num_B) + 'B'
