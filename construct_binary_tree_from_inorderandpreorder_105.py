class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # same as postorder and inorder
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None
        
        def dfs(preorder, inorder, pre_start, pre_end, in_start, in_end):
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            index = inorder.index(root.val)
            diff = index - in_start
            root.left = dfs(preorder, inorder, pre_start+1, pre_start+diff, in_start, in_start+diff-1) if in_start != index else None
            root.right = dfs(preorder, inorder, pre_start+diff+1, pre_end, index+1, in_end) if index != in_end else None
            return root
        return dfs(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)
