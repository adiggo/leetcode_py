class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        
        #set up a fake node
        fakeNode = ListNode(0)
        firstTime = True
        res = None
        carrier = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            newVal = val1 + val2 + carrier
            carrier = newVal / 10
            tmpNode = ListNode(newVal % 10)
            fakeNode.next = tmpNode
            fakeNode = fakeNode.next
            # keep record linklist starter
            if firstTime:
                res = tmpNode
                firstTime = False
        if carrier > 0:
            tmpNode = ListNode(carrier)
            fakeNode.next = tmpNode
        return res
