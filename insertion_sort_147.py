class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        fakeHead = ListNode(-1)
        fakeHead.next = head
        next = head.next
        head.next = None
        cur = next
        tail = head
        # record a tail to avoid unnecessary check
        while cur:
            if cur.val >= tail.val:
                tail.next = cur
                next = cur.next
                cur.next = None
                tail = cur
                cur = next
            else:
                newCur = fakeHead.next
                prev = fakeHead
                while newCur and cur.val > newCur.val:
                    prev = newCur
                    newCur = newCur.next
                prev.next = cur
                next = cur.next
                cur.next = newCur
                cur = next
        return fakeHead.next
