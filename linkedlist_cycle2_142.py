# additional space
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes = set()
        while head:
            if head in nodes:
                return head
            else:
                nodes.add(head)
                head = head.next
        return None

# constant space
class Solution2(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        slow, fast = head, head
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            if not fast:
                return None
            else:
                if slow == fast:
                    break
        cur = head
        while cur:
            if cur is slow:
                return cur
            cur = cur.next
            slow = slow.next
        return None
