class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # check whethere numbers are additive
        # what is additive
        # some case need to take case: no preceding zeros
        # for the follow up, we need to use biginteger class in java
        # in python, it has been automatically resolved
        if len(num) < 3:
            return False
        l = len(num)
        # each time we only need to check max(l1, l2) and max(l1, l2)+1
        # i is the length of first num, j is the length of second num
        for i in xrange(1, l / 2 + 1):
            if self.isNumberValid(num, 0, i):
                n1 = long(num[:i])
                j = 1
                while l - j - i >= max(i, j):
                    if self.isNumberValid(num, i, i + j):
                        n2 = long(num[i:i + j])
                        max_l = max(i, j)
                        if self.isNumberValid(num, i + j, i + j + max_l):
                            n3 = long(num[i + j: i + j + max_l])
                            if n1 + n2 == n3 and self.checkAdditive(num, i + j + max_l, n2, n3, max_l):
                                return True
                            else:
                                if l - j - i >= max_l + 1:
                                    if self.isNumberValid(num, i + j, i + j + max_l + 1):
                                        n3 = long(num[i + j: i + j + max_l + 1])
                                        if n1 + n2 == n3 and self.checkAdditive(num, i + j + max_l + 1, n2, n3,
                                                                                max_l + 1):
                                            return True
                    j += 1
            else:
                return False
        return False

    def checkAdditive(self, num, cur, n1, n2, max_l):
        if cur >= len(num):
            return True
        if cur + max_l <= len(num):
            if self.isNumberValid(num, cur, cur + max_l):
                n3 = long(num[cur: cur + max_l])
                if n1 + n2 == n3:
                    return self.checkAdditive(num, cur + max_l, n2, n3, max_l)
                else:
                    if cur + max_l + 1 <= len(num):
                        n3 = long(num[cur: cur + max_l + 1])
                        if n1 + n2 == n3:
                            return self.checkAdditive(num, cur + max_l + 1, n2, n3, max_l + 1)
                    else:
                        return False
            else:
                return False

    # if a number starts with 0, then it is valid only its length is 0
    def isNumberValid(self, num, i, j):
        if num[i] == '0' and j - i > 1:
            return False
        if num[i] == '0' and j - i == 1:
            return True
        return True if j > i else False


# second round
class Solution2(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) < 3:
            return False
        l = len(num)
        # each time we only need to check max(l1, l2) and max(l1, l2)+1
        # i is the length of first num, j is the length of second num
        for i in xrange(1, l / 2 + 1):
            # check the number is valid
            if self.number_valid(num, 0, i):
                n1 = int(num[:i])
                j = 1
                while l - j - i >= max(i, j):
                    if self.number_valid(num, i, i + j):
                        n2 = int(num[i:i + j])
                        max_l = max(i, j)
                        n3 = [int(num[i + j: i + j + max_l]) if self.number_valid(num, i + j, i + j + max_l) else None, int(num[i + j: i + j + max_l + 1]) if self.number_valid(num, i + j, i + j + max_l + 1) else None]
                        if n1 + n2 in n3:
                            if n1 + n2 == n3[0] and self.is_additive(num, i + j + max_l, n2, n3[0], max_l):
                                return True
                            elif n1 + n2 == n3[1] and self.is_additive(num, i + j + max_l + 1, n2, n3[1], max_l + 1):
                                return True
                    j += 1

        return False

    def is_additive(self, num, cur, n1, n2, max_l):
        # base condition
        if cur >= len(num):
            return True
        
        if cur + max_l <= len(num):
            if self.number_valid(num, cur, cur + max_l):
                n3 = [int(num[cur: cur + max_l]), int(num[cur: cur + max_l + 1]) if self.number_valid(num, cur, cur + max_l + 1) else None]
                if n1 + n2 in n3:
                    if n1 + n2 == n3[0]:
                        return self.is_additive(num, cur + max_l, n2, n3[0], max_l)
                    elif n1 + n2 == n3[1]:
                        return self.is_additive(num, cur + max_l + 1, n2, n3[1], max_l + 1)
        return False

    # if a number starts with 0, then it is valid only its length is 0
    def number_valid(self, num, i, j):
        if num[i] == '0' and j - i > 1:
            return False
        if num[i] == '0' and j - i == 1:
            return True
        return True if j > i else False
