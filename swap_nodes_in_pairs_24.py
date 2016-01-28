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
