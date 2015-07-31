class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA == headB:
            return headA
        if not headA or not headB:
            return None
        rootA, rootB, lengthA, lengthB = headA, headB, 1, 1
        while rootA.next:
            rootA, lengthA = rootA.next, lengthA+1
        while rootB.next:
            rootB, lengthB = rootB.next, lengthB + 1
        if rootA != rootB:
            return None
        if lengthA > lengthB:
            for i in range(lengthA - lengthB):
                headA = headA.next
            while headA and headB:
                if headA == headB:
                    return headA
                headA, headB = headA.next, headB.next
        elif lengthA < lengthB:
            for i in range(lengthB - lengthA):
                headB = headB.next
            while headA and headB:
                if headA == headB:
                    return headA
                headA, headB = headA.next, headB.next
        elif lengthA == lengthB:
            while headA and headB:
                if headA == headB:
                    return headA
                headA, headB = headA.next, headB.next
        return None
