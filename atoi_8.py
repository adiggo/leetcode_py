class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # conver string to integer
        if not str:
            return 0
        str = str.strip()
        if not str:
            return 0
        # start with + or -
        # no space for two numbers
        if str.startswith('+'):
            return self.checkSignNumber('+', str)
        elif str.startswith('-'):
            return self.checkSignNumber('-', str)
        elif str[0] >= '0' and str[0] <= '9':
            i = 0
            while i < len(str):
                if str[i] >= '0' and str[i] <= '9':
                    i += 1
                    continue
                else:
                    break
            if i > 0:
                res = int(str[:i])
                return res if res <= 2147483647 else 2147483647
            else:
                return 0
        else:
            return 0

    def checkSignNumber(self, operator, str):
        is_positive = True if operator == '+' else False
        index = str.index(operator) + 1
        has_digit = False
        str = str[index:]
        index = 0
        while index < len(str):
            if str[index] <= '9' and str[index] >= '0':
                index += 1
                has_digit = True
                continue
            else:
                break
        if not has_digit:
            return 0
        else:
            if index == 0:
                return 0
            else:
                res = int(str[:index])
                if res > 2147483647:
                    return 2147483647 if is_positive else -2147483648
                else:
                    return res if is_positive else -res
            
