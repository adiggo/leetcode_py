class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # A, E , I, O, U
        char_list = list(s)
        vowels = set()
        for c in 'aeiouAEIOU':
            vowels.add(c)
        
        left, right = 0, len(s)-1
        while left < right:
            while char_list[left] not in vowels and left < right:
                left += 1
            # same char, no need to swap
            if left == right:
                break
            else:
                while char_list[right] not in vowels and right > left:
                    right -= 1
                if left == right:
                    break
                else:
                    char_list[left], char_list[right] = char_list[right], char_list[left]
            left += 1
            right -= 1
        return ''.join(char_list)
