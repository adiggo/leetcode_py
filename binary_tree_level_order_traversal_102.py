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


    def levelOrderDfs(self, root):
        res = []
        if not root:
            return res
        self.dfs(root, res, 0)
        return res
        
    def dfs(self, root, res, level):
        if not root:
            return
        if level < len(res):
            res[level].append(root.val)
        else:
            # only works for the most left node in each level
            res.append([root.val])
        self.dfs(root.left, res, level+1)
        self.dfs(root.right, res, level+1)
