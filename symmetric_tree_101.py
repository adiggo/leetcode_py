# recursion
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #root.left  --> root.right
        #root.left.right --> root.right.left
        #root.left.left --> root.right.right
        if not root:
            return True
        return self.isMirror(root.left, root.right)
            
    def isMirror(self, left, right):
        if not left and not right:
            return True
        if left and right and left.val == right.val:
            if self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left):
                return True
        return False

# iterative
class Solution2(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #root.left  --> root.right
        #root.left.right --> root.right.left
        #root.left.left --> root.right.right
        if not root:
            return True
        queue = []
        queue.append(root)
        while queue:
            newQueue = []
            left, right = 0, len(queue)-1
            while left < len(queue):
                if left <= right:
                    lleft = queue[left].left.val if queue[left].left else None
                    rright = queue[right].right.val if queue[right].right else None
                    lright = queue[left].right.val if queue[left].right else None
                    rleft = queue[right].left.val if queue[right].left else None
                    if lleft != rright or lright != rleft:
                        return False
                    right -= 1
                if queue[left].left:
                    newQueue.append(queue[left].left)
                if queue[left].right:
                    newQueue.append(queue[left].right)
                left += 1
            queue = newQueue
        return True 
