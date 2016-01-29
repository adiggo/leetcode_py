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
        
