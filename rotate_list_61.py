class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        start, l = head, 1
        end = start
        while start.next:
            start = start.next
            if not start.next:
                end = start
            l += 1
        k = (l - k % l) % l
        if k == 0:
            return head
        root = head
        while k > 1:
            root = root.next
            k -= 1
        # swap
        tmp, root.next = root.next, None
        end.next = head
        return tmp
