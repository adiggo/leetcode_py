class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        if not s or len(s) > 3 * 4 or len(s) < 4:
            return res
        # valid IP address: at most 255 since each octet has 8 bits, so range is 0 to 255
        self.back_track(s, 0, res, [], 0)
        ips = []
        for oct in res:
            ips.append('.'.join(oct))
        return ips
        
    # backtracking 
    def back_track(self, s, index, res, cur, l):
        if len(cur) == 4 and index == len(s):
            res.append(list(cur))
            return
        for i in xrange(3):
            if len(s) - 1 - l - i > (4 - len(cur) - 1) * 3:
                continue
            if len(s) -1 - l - i < 3 - len(cur):
                continue
            # check special case such as: 001, 01
            if i > 0 and s[index] == '0':
                break
            # check right bound
            if i == 2 and self.__get_octet_value(s[index: index + 3]) > 255:
                continue
            cur.append(s[index: index + i + 1])
            self.back_track(s, index + i + 1, res, cur, l + i + 1)
            cur.pop()
            
    def __get_octet_value(self, l):
        res = 0
        for i in l:
            res = 10 * res + int(i)
        return res
