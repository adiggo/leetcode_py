class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # preorder
        self.__dfs(root)
        return
        
    def __dfs(self, root):
        if not root:
            return None, None
        if not root.left and not root.right:
            return root, root
        left, left_tail = self.__dfs(root.left)
        right_node = root.right
        # if left is not None, then set root.right = left
        if left:
            root.right = left
            # remove left tree relation
            root.left = None
        right, right_tail = self.__dfs(right_node)
        if left_tail:
            left_tail.right = right
        # if right_tail is None, then use left_tail as the tail of the sub root
        return root, right_tail if right_tail else left_tail
