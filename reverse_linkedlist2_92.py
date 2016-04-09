class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        fakeHead = ListNode(-1)
        fakeHead.next = head
        prev, cur = fakeHead, head
        mPrev = None
        i = 1
        while cur:
            # reverse list
            local_next = cur.next
            if i <= n and i >= m:
                if i == m:
                    mPrev = prev
                else:
                    cur.next = prev
                if i == n:
                    nth = mPrev.next
                    mPrev.next = cur
                    nth.next = local_next
            prev = cur
            cur = local_next
            i += 1
        return fakeHead.next
