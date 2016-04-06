oclass Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # get length of list A and B
        lA, lB = 0, 0
        curA, curB = headA, headB
        while curA:
            curA = curA.next
            lA += 1
        while curB:
            curB = curB.next
            lB += 1
        diff = abs(lA - lB)
        return self.__getIntersectionNode(headA, headB, diff) if lA > lB else self.__getIntersectionNode(headB, headA, diff)
        
    def __getIntersectionNode(self, head1, head2, diff):
        # list1 has more diff length than list2
        while diff > 0:
            head1 = head1.next
            diff -= 1
        
        while head1 and head2:
            if head1.val == head2.val:
                return head1
            else:
                head1, head2 = head1.next, head2.next
        return None
