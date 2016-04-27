class Solution(object):
    # bfs looking for shortest path. 
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s: return ['']
        # use vis to check all visted elements
        queue, res, visited = collections.deque(), [], set([s])
        queue.append(s)
        found = False
        while queue:
            cur = queue.popleft()
            # once we found the valid one, we will not go to next level. Which means we will insert elements into queue.
            if self.isValidParentheses(cur):
                found = True
                res.append(cur)
            elif not found:
                for i in xrange(len(cur)):
                    if cur[i] == '(' or cur[i] == ')':
                        t = cur[:i] + cur[i + 1:]
                        if t not in visited:
                            queue.append(t)
                            visited.add(t)
        return res
 
    # check whethere a string is valid parenthesis format
    def isValidParentheses(self, s):
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                if cnt == 0: return False
                cnt -= 1
        return cnt == 0



    # dfs
    def removeInvalidParenthesesDFS(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s: 
            return ['']
        left_remove = right_remove = 0
        for c in s:
            if c == '(':
                left_remove += 1
            elif c == ')':
                if left_remove:
                    left_remove -= 1
                else:
                    right_remove += 1
        # use a set to hold all valid result
        ans = set()
        self.dfs(0, left_remove, right_remove, 0, '', s, ans)
        return list(ans)
 
    # open parent means is there any open parents "("
    def dfs(self, index, left_remove, right_remove, open_parents, cur, s, ans):
        # base case: left_remove, right_remove, open_parents < 0
        if left_remove < 0 or right_remove < 0 or open_parents < 0:     
            return
        if index == len(s):
            # add cur back to set if any of left_remove, right_remove, open_parents are 0
            if left_remove == right_remove == open_parents == 0:
                ans.add(cur)
            return
        if s[index] == '(':
            self.dfs(index + 1, left_remove - 1, right_remove, open_parents, cur, s, ans)
            self.dfs(index + 1, left_remove, right_remove, open_parents + 1, cur + s[index], s, ans)
        elif s[index] == ')':
            self.dfs(index + 1, left_remove, right_remove - 1, open_parents, cur, s, ans)
            self.dfs(index + 1, left_remove, right_remove, open_parents - 1, cur + s[index], s, ans)
        else:
            self.dfs(index + 1, left_remove, right_remove, open_parents, cur + s[index], s, ans)
