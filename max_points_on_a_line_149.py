class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points:
            return 0
    
        res = 1
        for i in xrange(len(points)):
            slopes = dict()
            dup = 0
            same_x_num = 0
            for j in xrange(i+1, len(points)):
                v, status = self.__get_slope(points[i], points[j])
                if status == 1:
                    dup += 1
                elif status == 2:
                    same_x_num += 1
                elif status == 3:
                    slopes[v] = slopes.get(v, 0) + 1
            
            res = max(res, same_x_num + dup + 1)
            for key in slopes:
                res = max(dup + slopes[key] + 1, res)
        return res
        
    # three status: 1. same location 2. their x value same 3. normal case
    def __get_slope(self, p1, p2):
        if p1.x == p2.x and p1.y != p2.y:
            return 0, 2
        if p1.x == p2.x and p1.y == p2.y:
            return 0,1
        return float(p2.y - p1.y)/float(p2.x - p1.x) , 3



# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
class Solution2:
    # @param {int[]} points an array of point
    # @return {int} an integer
    def maxPoints(self, points):
        # Write your code here
        if not points:
            return 0
        l = len(points)
        res = 0
        for i in xrange(l):
            p1 = points[i]
            infinite_slope = 1
            dup = 0
            slope_map = dict()
            for j in xrange(i+1, l):
                p2 = points[j]
                x_diff = p2.x - p1.x
                y_diff = p2.y - p1.y
                if x_diff == 0 and y_diff == 0:
                    dup += 1
                elif x_diff == 0:
                    infinite_slope += 1
                else:
                    divisor = self.gcd(y_diff, x_diff)
                    slope = (y_diff/divisor, x_diff/divisor)
                    slope_map[slope] = slope_map.get(slope, 1) + 1
            for k in slope_map:
                res = max(slope_map.get(k) + dup, res)
            res = max(res, infinite_slope + dup)
            
        return res
        
        
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a%b)
