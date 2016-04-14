class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        
        #skip first level, since there is no next pointer for root
        while root:
            next_first = None
            prev = None
            while root:
                if not next_first:
                    next_first = root.left if root.left else root.right
                if root.left:
                    if prev:
                        prev.next = root.left
                    prev = root.left
                if root.right:
                    if prev:
                        prev.next = root.right
                    prev = root.right
                root = root.next
            root = next_first
