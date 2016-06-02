class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # the idea is to first calculate all the frequency of char in the string
        # traverse the string, reduce the frequency by one based on the char each time
        # if the last element in the stack is larger than the current char and its corresponding count is still larger than zero, then we can remove the last char from the stack, do this process until it does not met the condition, each time also mark the correponding's char visited as false.
        # append the character
        visited, cnt = [False] * 26, [0] * 26
        res = []
        # calculate frequences
        for c in s:
            cnt[ord(c) - ord('a')] += 1  # ord(a) =97
        
        for c in s:
            index = ord(c) - ord('a')
            cnt[index] -= 1
            if visited[index]:
                continue
            while res and res[-1] > c and cnt[ord(res[-1]) - ord('a')]:
                visited[ord(res.pop()) - ord('a')] = False
            res.append(c)
            visited[index] = True
        return ''.join(res)
