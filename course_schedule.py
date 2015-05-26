class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        #dfs
        helper = [0] * numCourses
        if prerequisites is None or len(prerequisites) == 0:
            return True
        adj_dict = init_adj(prerequisites)
        for vertex in adj_dict.keys():
            if helper[vertex] == 0:
                if self.dfs(adj_dict, vertex, helper):
                    continue
                else:
                    return False
        return True

    def dfs(self, adj_dict, vertex, helper):
        helper[vertex] = 1
        if adj_dict.get(vertex) is not None:
            for child in adj_dict.get(vertex):
                if helper[child] == 0 and not self.dfs(adj_dict, child, helper):
                    return False
                if helper[child] == 1:
                    return False
        helper[vertex] = 2
        return True

def init_adj(prerequisites):
    dict = {}
    for tmp in prerequisites:
        list = []
        if dict.get(tmp[1]) is not None:
            dict.get(tmp[1]).append(tmp[0])
        else:
            list.append(tmp[0])
            dict[tmp[1]] = list
    return dict
