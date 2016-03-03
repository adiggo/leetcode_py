class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # just modify the value
        if not node:
            return
        prev = None
        while node.next:
            node.val = node.next.val
            prev = node
            node = node.next
        prev.next = None
