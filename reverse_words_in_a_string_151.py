class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # idea is to reverse the whole string
        # then reverse each word
        s = s[::-1]
        i = 0
        arr = s.split()
        for i in xrange(len(arr)):
            arr[i] = arr[i][::-1]
        return ' '.join(arr)
        


class Solution2(object):
       # @param s, a string
    # @return a string
    def reverseWords(self, s):
        words = s.split()
        words.reverse()
        return " ".join(words) 
