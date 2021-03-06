class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        # complete binaru tree, so we only need to count the height
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
