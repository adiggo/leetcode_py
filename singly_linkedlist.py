class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        cur = head
        prev = None
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = nexti
        #remember to return prev, not head
        return prev
