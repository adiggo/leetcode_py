class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1 = set()
        for n in nums1:
            n1.add(n)
        res = set()
        for n in nums2:
            if n in n1:
                res.add(n)
        return list(res)
