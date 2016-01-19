class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []

        cur_res = []
        if digits is None or len(digits) == 0:
            return []
        self.dfs(res, 0, digits, cur_res)
        return res

    def dfs(self, res, i, digits, cur_res):
        if len(cur_res) == len(digits):
            # copy the result into a tmp list
            str1 = ''.join(str(e) for e in cur_res)
            res.append(str1)
            return
        letters = self.get_letter(digits[i])
        for letter in letters:
            cur_res.append(letter)
            self.dfs(res, i + 1, digits, cur_res)
            del cur_res[len(cur_res) - 1]

    # special 7 and 9, use char() and ord() to convert char, int
    def get_letter(self, digit):
        digit = int(digit)
        if digit < 2 or digit > 9:
            return []
        left = 2
        right = 9
        diff = digit - left
        c_ord_left = ord('a') + 3 * diff + 1 if diff == 6 or diff == 7 else ord('a') + 3 * diff
        c_ord_right = c_ord_left + 2 if diff == 6 or diff < 5 else c_ord_left + 3
        chars = []
        for i in range(c_ord_left, c_ord_right + 1):
            chars.append(chr(i))
        return chars
