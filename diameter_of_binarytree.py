
# native approach is calculate each node's longest path, and for each node, the longest path = max_depth(node.left) + max_depth(node.right)
# but this basically duplicate the calculation, so use multiple value as the return value, store the max_depth as the second params of response
class BinaryTreeDiameter(object):
    def get_diameter(self, root):
        d, depth = self.diameter(root)
        return d
    def diameter(self, root):
        d, depth = 0, 0
        if not root:
            return d, depth
        leftD, d1 = self.diameter(root.left)
        rightD, d2 = self.diameter(root.right)
        depth = max(d1, d2) + 1
        d = d1 + d2 + 1
        d = max(leftD, rightD, d)
        return d, depth


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)

n1.left = n2
n1.right = n3

n2.right = n4

b = BinaryTreeDiameter()
print b.get_diameter(n1)
