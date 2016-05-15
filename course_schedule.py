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



# second round
# compare this problem with graph valid tree
class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        #dfs
        if not prerequisites or len(prerequisites) == 0:
            return True
        visited = [0] * numCourses
        adj = self.init_adj(prerequisites)
        for course in adj:
            if visited[course] == 0:
                if self.has_cycle(adj, course, visited):
                    continue
                else:
                    return False
        return True

    def has_cycle(self, adj, course, visited):
        # set color as gray
        visited[course] = 1
        children = adj.get(course)
        if children:
            for next_course in children:
                if visited[next_course] == 1:
                    return False
                if visited[next_course] == 0 and not self.has_cycle(adj, next_course, visited):
                    return False
        visited[course] = 2
        return True
        
    def init_adj(self, prerequisites):
        adj = dict()
        for courses in prerequisites:
            if courses[1] in adj:
                adj.get(courses[1]).append(courses[0])
            else:
                adj[courses[1]] = [courses[0]]
        return adj




class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        #dfs
        if not prerequisites or len(prerequisites) == 0:
            return True
        visited = [0] * numCourses
        adj, degree = self.init_adj(prerequisites, numCourses)
        queue = collections.deque()
        for i in xrange(numCourses):
            if degree[i] == 0:
                queue.append(i)
        while queue:
            course = queue.popleft()
            children = adj.get(course)
            if children:
                for course in adj.get(course):
                    degree[course] -= 1
                    if degree[course] == 0:
                        queue.append(course)
        for i in xrange(numCourses):
            if degree[i] != 0:
                return False
        return True

    def init_adj(self, prerequisites, n):
        adj = dict()
        degree = [0] * n
        for courses in prerequisites:
            if courses[1] in adj:
                adj.get(courses[1]).append(courses[0])
            else:
                adj[courses[1]] = [courses[0]]
            degree[courses[0]] += 1
        return adj, degree
