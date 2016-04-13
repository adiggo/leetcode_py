class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        self.connectNext(root, None)
        
    def connectNext(self, root, left):
        if not root:
            return
        if not root.left and not root.right:
            if left:
                left.next = root
            return
        if left:
            left.next = root
            self.connectNext(root.left, left.right)
        else:
            self.connectNext(root.left, None)
        self.connectNext(root.right, root.left)
        
