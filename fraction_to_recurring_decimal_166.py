class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return str(0)
        flag = True if numerator > 0 and denominator > 0 or numerator < 0 and denominator < 0 else False
        numerator = abs(numerator)
        denominator = abs(denominator)
        fractions_dict = dict()
        curD = numerator / denominator
        f = numerator % denominator
        if f == 0:
            return str(curD) if flag else '-' + str(curD)

        i = 0
        fractions_l = []
        f = f * 10
        while f not in fractions_dict:
            fractions_dict[f] = i
            while f < denominator:
                f *= 10
                i += 1
                fractions_l.append(str(0))
                fractions_dict[f] = i
                
            d = f / denominator 
            fractions_l.append(str(d))
            f = f % denominator
            if f == 0:
                return str(curD) + '.'+''.join(fractions_l) if flag else '-'+str(curD) + '.'+''.join(fractions_l)
            i += 1
            f = f * 10
            
        start, end = fractions_dict[f], i
        res = str(curD) + '.' + ''.join(fractions_l[:start]) + '(' + ''.join(fractions_l[start:end]) + ')'
        return res if flag else '-'+res
       

# a clean code: use hashmap to store all remainders
class Solution2(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return str(0)
        flag = True if numerator > 0 and denominator > 0 or numerator < 0 and denominator < 0 else False
        numerator = abs(numerator)
        denominator = abs(denominator)
        fractions_dict = dict()
        curD = numerator / denominator
        i = 0
        fractions_l = []
        loc = 0
        while True:
            fractions_l.append(str(numerator/denominator))
            i += 1
            numerator = numerator%denominator * 10
            if numerator == 0:
                break
            if numerator in fractions_dict:
                loc =  fractions_dict[numerator]
                break
            fractions_dict[numerator] = i
        if len(fractions_l) == 1:
            res = str(fractions_l[0])
            return res if flag else '-' + res
        else:
            if loc == 0:
                res = str(fractions_l[0]) + '.' + ''.join(fractions_l[1:])
                return res if flag else '-'+ res
            else:
                res = str(fractions_l[0]) + '.' + ''.join(fractions_l[1:loc]) + '(' + ''.join(fractions_l[loc:i]) + ')'
                return res if flag else '-'+ res

         
