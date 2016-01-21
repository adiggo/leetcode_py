class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []
        fake_root = root
        if root is not None:
            self.stack.append(root)
            while fake_root.left is not None:
                self.stack.append(fake_root.left)
                fake_root = fake_root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stack) == 0:
            return False
        return True

    def next(self):
        """
        :rtype: int
        """
        # this only occupy O(h) memory space
        if self.hasNext:
            next_node =  self.stack.pop()
            if next_node.right is not None:
                self.stack.append(next_node.right)
                right_node = next_node.right
                while right_node.left is not None:
                    self.stack.append(right_node.left)
                    right_node = right_node.left
            return next_node.val
        else:
            return 0
