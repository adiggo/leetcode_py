class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)
        if not head.next.next:
            root = TreeNode(head.val)
            root.right = TreeNode(head.next.val)
            return root
        slow, fast, root = head, head, head
        while fast:
            tmp = slow
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
                if not fast:
                    root.next = None
            else:
                root.next = None
            root = tmp
        tree_root = TreeNode(root.val)
        tree_root.left = self.sortedListToBST(head)
        tree_root.right = self.sortedListToBST(slow)
        return tree_root
