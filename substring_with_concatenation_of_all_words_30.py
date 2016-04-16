class Solution(object):
    def findSubstring(self, s, words):
        res = []
        if not s or not words or len(s) < len(words[0]) * len(words):
            return res
        l = len(words[0])
        total_l = l * len(words)
        word_map = dict()
        for word in words:
            word_map[word] = word_map.get(word, 0) + 1
        for i in xrange(l):
            right, left = i, i
            cur_map = dict(word_map)
            while right + l <= len(s):
                status = 0
                while right - left <= total_l and right + l <= len(s):
                    word = s[right: right + l]
                    right += l
                    if word not in cur_map:
                        status = 2
                        break
                    cur_map[word] = cur_map.get(word, 0) - 1
                    if cur_map.get(word) < 0:
                        status = 3
                        break
                    if right - left == total_l:
                        status = 1
                        break
                if not status:
                    break
                elif status == 1:
                    res.append(right - total_l)
                    cur_map[s[right - total_l:right - total_l + l]] = cur_map.get(
                        s[right - total_l:right - total_l + l], 0) + 1
                    left += l
                elif status == 2:
                    cur_map = dict(word_map)
                    left = right
                elif status == 3:
                    while left + l <= right:
                        prev_word = s[left: left + l]
                        cur_map[prev_word] = cur_map.get(prev_word, 0) + 1
                        if s[right - l:right] == prev_word:
                            left += l
                            break
                        left += l
        return res
