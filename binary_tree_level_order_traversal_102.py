class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        res.append([root.val])
        level_nodes = [root]
        while True:
            cur_level = []
            for node in level_nodes:
                if node.left:
                    cur_level.append(node.left)
                if node.right:
                    cur_level.append(node.right)
            if not cur_level:
                break
            level_nodes = cur_level
            res.append([x.val for x in level_nodes])
        return res
       

    
    def levelOrder2(self, root):
        res = []
        if not root:
            return res
        res.append([root.val])
        level_nodes = [root]
        while level_nodes:
            cur_level = []
            length = len(level_nodes)
            for i in range(length):
                node = level_nodes[0]
                del level_nodes[0]
                if node.left:
                    cur_level.append(node.left.val)
                    level_nodes.append(node.left)
                if node.right:
                    cur_level.append(node.right.val)
                    level_nodes.append(node.right)
            if cur_level:
                res.append(cur_level)
        return res
