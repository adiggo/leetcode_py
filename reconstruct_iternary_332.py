class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # use map, key --> from, value --> to
        iternaries = {}
        for ticket in tickets:
            if ticket[0] not in iternaries:
                iternaries[ticket[0]] = [ticket[1]]
            else:
                iternaries[ticket[0]].append(ticket[1])
        visited = dict()
        for f in iternaries:
            iternaries[f].sort()
            visited[f] = [False] * len(iternaries.get(f))
        
        res = []
        f = 'JFK'
        res.append(f)
        self.dfs(f, res, visited, iternaries, len(tickets)+1)
        return res
        
    def dfs(self, f, res, visited, iternaries, l):
        if len(res) == l:
            return True
        dests = iternaries.get(f)
        if not dests:
            return False
        for i in xrange(len(dests)):
            if not visited.get(f)[i]:
                visited.get(f)[i] = True
                res.append(dests[i])
                if self.dfs(dests[i], res, visited, iternaries, l):
                    return True
                res.pop()
                visited.get(f)[i] = False
        return False

