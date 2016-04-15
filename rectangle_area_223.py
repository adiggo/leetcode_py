class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # A < C,  E < G, B < D, F < H
        # intersection condition
        l = min(C, G) - max(A, E)
        h = min(D, H) - max(B, F)
        res = (C-A) * (D-B) + (G-E)* (H-F)
        if l > 0 and h > 0:
            return res - l*h
        else:
            return res
