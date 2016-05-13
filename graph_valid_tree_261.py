class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        # no cycle in tree
        # the main idea: starting from any point, no cycle exist
        if not edges:
            return False if n > 1 else True
        if n > len(edges) + 1:
            return False
        adj, visited = self.preProcessing(edges)
        count = 0
        for e in edges:
            if not visited[e[0]]:
                count += 1
                if self.dfs(e[0], visited, adj, -1):
                    return False
        return True if count == 1 else False
            
                
        
    def dfs(self, v, visited, edges_map, parent):
        children = edges_map.get(v)
        visited[v] = True
        for c in children:
            if not visited[c]:
                if self.dfs(c, visited, edges_map, v):
                    return True
            elif c != parent:
                return True
        return False
        
        
    def preProcessing(self, edges):
        res = dict()
        visited = dict()
        for e in edges:
            if e[0] in res:
                res[e[0]].append(e[1])
            else:
                res[e[0]] = [e[1]]
            if e[1] in res:
                res[e[1]].append(e[0])
            else:
                res[e[1]] = [e[0]]
        for k in res:
            visited[k] = False
        return res, visited
