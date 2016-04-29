class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        # our aim is to find the longest palindrome with from string index of s[0]
        # abac#caba  --> 
        reverse_s = s[::-1]
        l = s + '#' + reverse_s
        next = [0] * len(l)
        for i in range(1, len(l)):
            j = next[i-1]
            while j > 0 and l[j] != l[i]:
                j = next[j-1]
            next[i] = j + (l[i] == l[j])
        return reverse_s[: len(s) - next[-1]] + s
