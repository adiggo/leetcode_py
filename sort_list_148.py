# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #merge sort
        if not head:
            return head
        if not head.next:
            return head
        slow, fast = head, head
        while fast:
            tmp = slow
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            # also cut relation between prev to mid
            if not fast:
                tmp.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.mergeList(left, right)
        
        
    # merge two sorted list
    def mergeList(self, left, right):
        if not left:
            return right
        if not right:
            return left
        fakeHead = ListNode(-1)
        lv, rv = left.val, right.val
        if lv < rv:
            fakeHead.next = left
            left = left.next
        else:
            fakeHead.next = right
            right = right.next
        prev = fakeHead.next
        while left or right:
            lv = left.val if left else sys.maxint
            rv = right.val if right else sys.maxint
            if lv < rv:
                prev.next = left
                left = left.next
            else:
                prev.next = right
                right = right.next
            prev = prev.next
        return fakeHead.next
