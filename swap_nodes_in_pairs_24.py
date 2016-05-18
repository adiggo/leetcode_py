class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fake_head = ListNode(-1)
        cur_node, prev_node = head, fake_head
        while cur_node:
            next_node = cur_node.next
            tmp_node = None
            if next_node:
                prev_node.next = next_node
                if next_node.next:
                    tmp_node = next_node.next
                # 2 -> 1
                next_node.next = cur_node
                cur_node.next = None
                prev_node = cur_node
                cur_node = tmp_node
            else:
                prev_node.next = cur_node
                cur_node = None
        return fake_head.next



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# second round
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        prev = dummy
        cur = head
        # 1 -> 2 -> 3 -> 4
        while cur:
            # 2
            next = cur.next if cur else None
            # 3
            nnext = next.next if next else None
            # d->2
            prev.next = next if next else cur
            # d->2->1
            if next:
                next.next = cur
            # break cur's previous relation
            cur.next = None
            # prev = 1
            prev = cur
            cur = nnext
            
        return dummy.next
