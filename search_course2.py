class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}

    def findOrder(self, numCourses, prerequisites):
        # used to store result
        #initialize dict
        reversePost = []
        checked = {}
        if prerequisites is None or len(prerequisites) == 0:
            return list(range(numCourses))
        dict = init_adj(prerequisites)
        for tmp in prerequisites:
            for tmpint in tmp:
                checked[tmpint] = 0
        for keys in dict.keys():
            if checked.get(keys) == 0:
                if self.dfs(keys, dict, checked, reversePost):
                    continue
                else:
                    return []
        reversePost.reverse()
        left = []
        if len(reversePost) < numCourses:
            for i in range(numCourses):
                if i not in reversePost:
                    left.append(i)
        reversePost.extend(left)
        return reversePost

    def dfs(self, key, dict, checked, reversePost):
        checked[key] = 1
        if get_adj(dict, key) is not None:
            for adj in get_adj(dict, key):
                if checked.get(adj) == 1:
                    return False
                if checked.get(adj) == 0 and not self.dfs(adj, dict, checked, reversePost):
                    return False
        checked[key] = 2
        reversePost.append(key)
        return True
#put everything into adj, so we can use without prerequisites
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
#get all of its adjacent list
def get_adj(dict, value):
    return dict.get(value)
