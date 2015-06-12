class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        #traverse tree
        helper = []
        head = root
        helper.append(root)
        while len(helper)>0:
            root = helper.pop()
            left = root.left
            right = root.right
            if left is not None:
                root.right = left
                helper.append(left)
            else:
                root.right = None
                
            if right is not None:
                root.left = right
                helper.append(right)
            else:
                root.left = None
        return head
