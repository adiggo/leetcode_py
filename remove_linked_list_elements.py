# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        if head is None:
            return head
        prev = None
        cur = head
        flag = False
        while cur:
            if cur.val == val:
                # update cur, not update prev, and also remove old cur node
                if not flag:
                    #update head
                    head = head.next
                tmp = cur.next
                if prev:
                    prev.next = cur.next
                cur.next = None
                cur = tmp
            else:
                flag = True
                prev = cur
                cur = cur.next
        return head
