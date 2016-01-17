class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_container = 0
        while left <= right and right < len(height):
            width = min(height[left], height[right])
            max_container = max(width * (right - left), max_container)
            # move the min of left and right
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_container
