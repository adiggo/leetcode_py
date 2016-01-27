class Solution(object):
    # if n > length, then we just remove nothing.
    def removeNthFromEnd(self, head, n):
         # find length
        fake_node = ListNode(-1)
        fake_node.next = head
        slow_node = fake_node
        fast_node = fake_node
        i = 0
        while fast_node is not None:
            if i == n:
                break
            fast_node = fast_node.next
            i+= 1
        prev = fake_node
        while fast_node is not None:
            prev = slow_node
            slow_node = slow_node.next
            fast_node = fast_node.next
        prev.next = slow_node.next
        slow_node.next = None
        return fake_node.next
