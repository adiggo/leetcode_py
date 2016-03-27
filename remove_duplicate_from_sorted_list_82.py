class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        fakeHead = ListNode(-1)
        fakeHead.next = head
        prev = head
        cur = head.next
        # global prev
        gprev = fakeHead
        while cur:
            flag = False
            while cur and cur.val == prev.val:
                flag = True
                prev = cur
                cur = cur.next
            if flag:
                gprev.next = cur
                prev.next = None
                prev, cur = cur, cur.next if cur else cur
            else:
                prev, gprev = cur, prev
                cur = cur.next
        return fakeHead.next
