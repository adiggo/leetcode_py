class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return None
        character_map = {}
        no_repeat_length = 0
        start, end = 0, 0
        for i, c in enumerate(s):
            # once find c in map, get the length of no repeat
            if c in character_map:
                end = i - 1
                cur_length = end - start + 1
                # update start position
                start = max(start, character_map.get(c)+1)
                no_repeat_length = max(no_repeat_length, cur_length)
                # update the map
                character_map[c] = i
            else:
                character_map[c] = i
        return max(len(s)-1-start+1, no_repeat_length)
