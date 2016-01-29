class Solution(object):
    def reverseKGroup(self, head, k):
        if k <= 1:
            return head
        cur_node = head
        l = 0
        while cur_node:
            l += 1
            cur_node = cur_node.next
        iteration = l / k
        fake_node = ListNode(-1)
        fake_node.next = head
        prev_node, cur_node = fake_node, head
        for i in range(iteration):
            prev_node, cur_node = self.reverse(cur_node,prev_node, k)
        if prev_node:
            prev_node.next = cur_node
        return fake_node.next
    # reverse the list
    # make sure k smaller than the length
    def reverse(self, node, prev_node, k):
        cur_node = node
        new_node = node.next
        while k - 1 > 0:
            k -= 1
            tmp = new_node.next if new_node else None
            new_node.next = cur_node
            cur_node = new_node
            new_node = tmp
        prev_node.next = cur_node
        return node, new_node
