class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # use stack to store paths
        # special char: ..   .  
        stack = []
        paths = path.split('/')
        for p in paths:
            if not p:
                continue
            if p == '.':
                continue
            elif p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        if not stack:
            return '/'
        else:
            return '/' + '/'.join(stack)
        
            
            
