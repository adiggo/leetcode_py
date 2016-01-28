class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        fake_node = ListNode(-1)
        cur_node = fake_node
        for i in range(len(lists)):
            # push a tuple contain the value and index in the lists
            # initial the heap
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, lists[i]))
        while heap:
            small_tuple = heapq.heappop(heap)
            cur_node.next = small_tuple[1]
            if small_tuple[1].next:
                heapq.heappush(heap, (small_tuple[1].next.val, small_tuple[1].next))
            cur_node = cur_node.next
        return fake_node.next
