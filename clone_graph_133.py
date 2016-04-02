class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return None
        helper = {node: UndirectedGraphNode(node.label)}
        s = collections.deque([(node, helper[node])])
        while s:
            cur, newCur = s.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in helper:
                    helper[neighbor] = UndirectedGraphNode(neighbor.label)
                    s.append((neighbor, helper[neighbor]))
                newCur.neighbors.append(helper[neighbor])
        return helper[node]
