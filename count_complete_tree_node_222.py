class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        # complete binary tree, so we only need to count the height
        # based on the completeness preperty:
        # if lefth == righh, then we know left half tree is fine, then we only need to calculate right half tree
        if not root:
            return 0
        lh = self.getHeight(root.left)
        rh = self.getHeight(root.right)
        if lh == rh:
            return (1<<lh) + self.countNodes(root.right)
        else:
            return (1<<rh) + self.countNodes(root.left)
            
    # get left height    
    def getHeight(self, node):
        height = 0
        while node:
            height, node = height+1, node.left
        return height


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# second round
class Solution2:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        # O(h ** 2)
        if not root:
            return 0
        l_h = self.get_height(root.left)
        r_h = self.get_height(root.right)
        if l_h == r_h:
            return (1 << l_h) + self.countNodes(root.right)
        else:
            return (1 << r_h )+ self.countNodes(root.left)
            
    # get left height    
    def get_height(self, node):
        height = 0
        while node:
            height, node = height+1, node.left
        return height
          
