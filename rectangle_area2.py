class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        # calculate the both area 
        length1 = abs(C-A)
        width1 = abs(D-B)
        area1 = length1 * width1
        length2 = abs(G-E)
        width2 = abs(H-F)
        area2 = length2 * width2
        area = area1 + area2
        # find situations when no intersect
        if H < B or E > C or F > D or A > G:
            return area
        # find intersect
        h1 = abs(max(A,E) - min(C,G))
        w1 = abs(max(B,F) - min(D,H))
        intersect = h1 * w1
        # total area - intersect
        return area - intersect
