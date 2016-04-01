class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        o = ListNode(-2)
        odd = ListNode(-1)
        even = o
        cur = head
        while cur:
            odd.next = cur
            even.next = cur.next
            odd = cur
            even = cur.next
            if cur.next:
                cur = cur.next.next
            else:
                break
        odd.next = o.next
        return head
