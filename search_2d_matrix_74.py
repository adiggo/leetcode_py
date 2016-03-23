class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # binary search in two dimension
        left, right  = 0, len(matrix)-1
        while left <= right:
            mid = left + (right - left)/2
            if target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][0]:
                left = mid + 1
            else:
                return True
        i = left
        if i == 0:
            return False
        i -= 1
        left, right = 0, len(matrix[0])-1
        while left <= right:
            mid = left + (right - left)/2
            if target < matrix[i][mid]:
                right = mid - 1
            elif target > matrix[i][mid]:
                left = mid + 1
            else:
                return True
        return False
