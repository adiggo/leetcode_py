class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        fake_node = ListNode(-1)
        cur_node = fake_node
        while l1 is not None or l2 is not None:
            l1_val = l1.val if l1 is not None else -sys.maxint -1 
            l2_val = l2.val if l2 is not None else -sys.maxint -1 
            if l1_val > l2_val:
                if l2 is None:
                    cur_node.next = l1
                    l1 = l1.next
                else:
                    cur_node.next = l2
                l2 = l2.next if l2 is not None else None
            else:
                if l1 is None:
                    cur_node.next = l2
                    l2 = l2.next
                else:
                    cur_node.next = l1
                l1= l1.next if l1 is not None else None
            cur_node = cur_node.next
        return fake_node.next
