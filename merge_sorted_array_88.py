class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i1, i2 = m-1, n-1
        while i1 >= 0 and i2 >= 0:
            if nums1[i1] > nums2[i2]:
                nums1[i1+i2+1] = nums1[i1]
                i1 -= 1
            else:
                nums1[i1+i2+1] = nums2[i2]
                i2 -= 1
        while i2 >= 0:
            nums1[i2] = nums2[i2]
            i2 -= 1
