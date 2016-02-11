class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        res = 0
        prev, local_sum = 0, 0
        index = height.index(max(height))
        for h in height[0:index+1]:
            if h < prev:
                local_sum += prev - h
            else:
                res += local_sum
                local_sum, prev = 0, h
        prev, local_sum= 0, 0
        for i in range(len(height)-1, index-1, -1):
            if height[i] >= prev:
                res += local_sum
                local_sum, prev = 0, height[i]
            else:
                local_sum += prev - height[i]
        return res

# use  stack to keep all decreasing trend numbers
    def trap2(self, A):
        """
        :type height: List[int]
        :rtype: int
        """
        if not A:
            return 0
        s = []
        cur, res = 0, 0
        while cur < len(A):
            while s and A[s[-1]] <= A[cur]:
                b = s.pop()
                if not s:
                    break
                # s[-1]-1
                res += (cur-s[-1]-1) * ((min(A[cur], A[s[-1]])) - A[b])
            s.append(cur)
            cur += 1
        return res
