class Solution(object):
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        total = m + n
        if total % 2 == 1:
            return self.findKthElement(A, B, total / 2 + 1)
        else:
            return float(self.findKthElement(A, B, total / 2) + self.findKthElement(A, B, total / 2 + 1)) / 2

    def findKthElement(self, A, B, k):
        if len(A) > len(B):
            return self.findKthElement(B, A, k)
        m, n = len(A), len(B)
        if m == 0:
            return B[k - 1]
        if k == 1:
            return min(A[0], B[0])
        a_i = min(k / 2, m)
        b_i = k - a_i
        if A[a_i - 1] < B[b_i - 1]:
            return self.findKthElement(A[a_i:], B, k - a_i)
        elif A[a_i - 1] > B[b_i - 1]:
            return self.findKthElement(A, B[b_i:], k - b_i)
        else:
            return A[a_i - 1]

