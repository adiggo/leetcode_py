class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map_helper = {}
        res = []
        for v in strs:
            char_cal = [0] * 26
            for c in v:
                index = ord(c) - ord('a')
                char_cal[index] += 1
            if tuple(char_cal) in map_helper:
                map_helper.get(tuple(char_cal)).append(v)
            else:
                map_helper[tuple(char_cal)] = [v]
        for i in map_helper:
            anagram_list = map_helper.get(i)
            anagram_list.sort()
            res.append(anagram_list)
        return res
