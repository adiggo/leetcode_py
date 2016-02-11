class Solution(object):
    # use several index to record the postion, this should save memory space.
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder or not inorder or len(inorder) != len(postorder):
            return None

        def dfs(inorder, postorder, in_start, in_end, post_start, post_end):
            root_val = postorder[post_end]
            root = TreeNode(root_val)
            inorder_index = inorder.index(root_val)i
            
            diff = inorder_index - in_start
            root.left = dfs(inorder, postorder, in_start, inorder_index - 1, post_start,
                            post_start + (diff - 1)) if inorder_index != in_start else None
            root.right = dfs(inorder, postorder, inorder_index + 1, in_end, post_start + diff,
                             post_end - 1) if inorder_index != in_end else None
            return root

        return dfs(inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1)
