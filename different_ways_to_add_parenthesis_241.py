class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        
        # divide conqueuer, calatan number
        
        result = []
        if not input:
            return result
        for i in xrange(len(input)):
            c = input[i]
            if not self.__isOps(c):
                continue
            left = self.diffWaysToCompute(input[:i])
            right = self.diffWaysToCompute(input[i+1:])
            
            for l in left:
                for r in right:
                    result.append(self.__calculate(l, r, c))
        if not result:
            result.append(int(input.strip()))
            
        return result
        
    def __isOps(self, c):
        if c == '+' or c == '-' or c =='*':
            return True
        else:
            return False
    
    def __calculate(self, num1, num2, ops):
        if ops == '+':
            return num1 + num2
        if ops == '-':
            return num1 - num2
        if ops == '*':
            return num1 * num2
        return None
        
