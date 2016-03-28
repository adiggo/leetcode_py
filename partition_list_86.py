class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        fakeHead = ListNode(-1)
        prev = fakeHead
        right = ListNode(-1)
        r = right
        cur = head
        while cur:
            if cur.val < x:
                prev.next = ListNode(cur.val)
                prev = prev.next
            else:
                r.next = ListNode(cur.val)
                r = r.next
            cur = cur.next
        prev.next = right.next
        return fakeHead.next
