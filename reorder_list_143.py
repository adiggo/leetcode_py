class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        slow = head
        fast = head
        # find mid node
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        # reverse mid to right list
        tmp = slow
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev, slow = slow, next
        
        while head or prev:
            if not prev:
                head.next = prev
                break
            else:
                next = head.next
                head.next = prev
                pnext = prev.next
                if next != tmp:
                    prev.next = next
                prev, head = pnext, next  
