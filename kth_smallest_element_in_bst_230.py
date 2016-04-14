class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return 0
        cur = root
        l = []
        while cur:
            l.append(cur)
            cur = cur.left
        index = 0
        while l:
            node = l.pop()
            index += 1
            if index == k:
                return node.val
            if node.right:
                node = node.right
                l.append(node)
                while node.left:
                    l.append(node.left)
                    node = node.left

class Solution2(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return 0
        
        left = self.countNumber(root.left) 
        if left == k-1:
            return root.val
        if left > k-1:
            return self.kthSmallest(root.left, k)
        elif left < k-1:
            return self.kthSmallest(root.right, k - left - 1)
    
        
    
    def countNumber(self, root):
        if not root:
            return 0
        return self.countNumber(root.left) + self.countNumber(root.right) + 1
