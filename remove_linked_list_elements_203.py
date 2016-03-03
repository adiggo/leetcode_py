class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        tmp = ListNode(-1)
        tmp.next = head
        prev = tmp
        cur = head
        while cur:
            next = cur.next
            if cur.val == val:
                prev.next = next
                cur.next = None
                cur = next
            else:
                prev = prev.next
                cur = cur.next
        return tmp.next
