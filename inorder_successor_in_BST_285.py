class Solution(object):
    def inorder_successor(self, node):
        if not node:
            return None

        def find_min(node):
            while node.left:
                node = node.left
            return node

        if node.right:
            return find_min(node.right)
        else:
            while node.parent:
                if node.parent.v > node.v:
                    return node.parent
            return None


class TreeNode(object):
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None
        self.parent = None
