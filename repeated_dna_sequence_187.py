class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s) <= 10:
            return []
        helper = {}
        for i in xrange(0, len(s)-10+1):
            sequence = s[i: i+10]
            if sequence in helper:
                helper[sequence] += 1
            else:
                helper[sequence] = 1
        res = []
        for sequence in helper:
            if helper[sequence] > 1:
                res.append(sequence)
        return res


#reference: http://bookshadow.com/weblog/2015/02/06/leetcode-repeated-dna-sequences/
class Solution2(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s) <= 10:
            return []
        map = {'A' : 0, 'C' : 1, 'G': 2, 'T' : 3}
        sum = 0
        helper = dict()
        res = []
        for i in xrange(len(s)):
            sum = (sum * 4 +  map[s[i]])
            if i < 9:
                continue
            helper[sum] = helper.get(sum, 0) + 1
            if helper.get(sum) == 2:
                res.append(s[i-9: i+1])
        return res
            
