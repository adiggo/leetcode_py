class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #reverse first half list
        fast = head
        slow = head
        prev = None
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev, slow = slow, next
        if prev:
            while prev:
                if prev.val != head.val:
                    return False
                else:
                    prev, head = prev.next, head.next
            return True
        else:
            return True
