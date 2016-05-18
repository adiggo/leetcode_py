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



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# second round
# merge two lists
class Solution2(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        prev = dummy
        while l1 or l2:
            v1 = l1.val if l1 else sys.maxint
            v2 = l2.val if l2 else sys.maxint
            if v1 < v2:
                prev.next = l1
                if l1:
                    prev = l1
                    l1 = l1.next
            else:
                prev.next = l2
                if l2:
                    prev = l2
                    l2 = l2.next
                
        return dummy.next
            
