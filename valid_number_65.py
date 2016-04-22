#http://blog.csdn.net/kenden23/article/details/18696083
class Solution(object):
    def isNumber(self, s):
        # need to build state automata
        INVALID=0; SPACE=1; SIGN=2; DIGIT=3; DOT=4; EXPONENT=5;
        #0invalid,1space,2sign,3digit,4dot,5exponent
        transitionTable=[[-1,  0,  3,  1,  2, -1],    #0 prev no input or just spaces 
                         [-1,  8, -1,  1,  4,  5],    #1 prev input is digits 
                         [-1, -1, -1,  4, -1, -1],    #2 prev no digits in front just Dot 
                         [-1, -1, -1,  1,  2, -1],    #3 prev sign 
                         [-1,  8, -1,  4, -1,  5],    #4 prev digits and dot in front 
                         [-1, -1,  6,  7, -1, -1],    #5 prev input 'e' or 'E' 
                         [-1, -1, -1,  7, -1, -1],    #6 after 'e' input sign 
                         [-1,  8, -1,  7, -1, -1],    #7 after 'e' input digits (only space, dot is valid)
                         [-1,  8, -1, -1, -1, -1]]    #8 after valid input input space (only space is valid)
        state=0; i=0
        while i<len(s):
            inputtype = INVALID
            if s[i]==' ': inputtype=SPACE
            elif s[i]=='-' or s[i]=='+': inputtype=SIGN
            elif s[i] in '0123456789': inputtype=DIGIT
            elif s[i]=='.': inputtype=DOT
            elif s[i]=='e' or s[i]=='E': inputtype=EXPONENT
            
            state=transitionTable[state][inputtype]
            if state==-1: 
                return False
            else: 
                i+=1
        # for the final state, only 1, 4, 7, 8 is valid
        return state == 1 or state == 4 or state == 7 or state == 8
