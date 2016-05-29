class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        # original node to new node
        helper = {}
        dummyNode = RandomListNode(head.label)
        prev = dummyNode
        helper[head] = dummyNode
        grandom = head.random
        while head.next:
            next = head.next
            if next:
                if next in helper:
                    prev.next = helper[next]
                else:
                    cur = RandomListNode(next.label)
                    helper[next] = cur
                    prev.next = cur
            random = head.random
            if random:
                if random in helper:
                    prev.random = helper[random]
                else:
                    r = RandomListNode(random.label)
                    helper[random] = r
                    prev.random = r
            prev, head = prev.next, head.next
            grandom = head.random
        if grandom:
            prev.random = helper[grandom] if grandom in helper else RandomListNode(grandom.label)
        return dummyNode

# second round
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        map = dict()
        dummy = RandomListNode(-1)
        prev = dummy
        while head:
            if head not in map:
                map[head] = RandomListNode(head.label)
            tmp = map.get(head)
            if head.random not in map:
                map[head.random] = RandomListNode(head.random.label) if head.random else None
            tmp.random = map.get(head.random)
            prev.next = tmp
            prev = tmp
            head = head.next
        return dummy.next
