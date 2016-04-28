class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        single = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        onedouble = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        double = [onedouble, 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        hundreds = [x + ' Hundred' for x in single]
        units= ['', 'Thousand', 'Million', 'Billion']
        units_name = set(['Thousand', 'Million', 'Billion'])
        map = {0: single, 1:double, 2: hundreds}
        if num == 0:
            return 'Zero'
        i = 0
        res = []
        prev = None
        while num > 0:
            r = num % 10
            j = i % 3
            #check for billion-million-thousand
            if j == 0 and i/3 > 1:
                if res[-1] in units_name:
                    res.pop()
                    
            unit = units[i/3] if j == 0 else ''
            if r == 0:
                if unit:
                    res.append(unit)
            else:
                j = i % 3
                unit = units[i/3] if j == 0 else ''
                number = ''
                # special for onedoubles
                if j == 1 and r == 1:
                    if prev != 0:
                        res.pop()
                    number = map[j][r-1][prev]
                else:
                    number = map[j][r-1]
                if unit:
                    res.append(unit)
                res.append(number)
                
            prev = r
            i += 1
            num /= 10
        return ' '.join(reversed(res))
