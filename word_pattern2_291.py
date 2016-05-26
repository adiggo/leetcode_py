class Solution(object):
    def words_pattern2(self, pattern, str):
        # backtracking
        # start from 1 to 1, 1 to 2 ....(n-index)
        if len(str) < len(pattern):
            return False
        return self.backtrack(pattern, str, 0, 0, dict(), set())

    # once there is a possible combination lead to True, then we return true
    def backtrack(self, pattern, str, index1, index2, str_map, str_set):
        # base condition check
        if index1 == len(pattern) and index2 == len(str):
            return True

        l1, l2 = len(pattern), len(str)
        letter = pattern[index1]
        for i in xrange(index2, l2 - (l1 - index1) + 1):
            word = str[index2: i + 1]
            if letter not in str_map:
                if word in str_set:
                    continue
                str_map[letter] = word
                str_set.add(word)
                match = self.backtrack(pattern, str, index1 + 1, i + 1, str_map, str_set)
                if match:
                    return True
                str_set.remove(word)
                str_map.pop(letter)
            else:
                if word != str_map[letter]:
                    continue
                else:
                    match = self.backtrack(pattern, str, index1 + 1, i + 1, str_map, str_set)
                    if match:
                        return True
                    else:
                        continue
        return False

