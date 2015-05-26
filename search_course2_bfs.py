class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}

    def findOrder(self, numCourses, prerequisites):
        # used to store result
        #initialize dict
        prenode = {}
        node_depend_number = [0] * numCourses
        for i in prerequisites:
            if not i[0] in prenode:
                prenode[i[0]] = []
            prenode.get(i[0]).append(i[1])
            node_depend_number[i[1]] = node_depend_number[i[1]] + 1
        queue = []
        for i in range(len(node_depend_number)):
            if node_depend_number[i] == 0:
                queue.append(i)
        res = []
        index = numCourses - 1
        while len(queue) != 0:
            key = queue.pop(0)
            res.insert(0, key)
            if key in prenode:
                for j in prenode.get(key):
                    node_depend_number[j] =node_depend_number[j] - 1
                    if node_depend_number[j] == 0:
                        queue.append(j)
            numCourses -= 1
        return res if numCourses == 0 else []
