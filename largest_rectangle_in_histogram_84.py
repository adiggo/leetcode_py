class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # when increase put value into stack
        # when decrease pop value larger than cur value
        stack = []
        res = 0
        i = 0
        while i < len(heights):
            if not stack:
                stack.append(i)
            else:
                if heights[i] >= heights[stack[-1]]:
                    stack.append(i)
                else:
                    k = stack.pop()
                    width = i if not stack else i - stack[-1] - 1
                    res = max(res, width * heights[k])
                    i -= 1
            i += 1
        while stack:
            k = stack.pop()
            # the first element in the stack should be the smallest element
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            res = max(res, width * heights[k])
        return res
