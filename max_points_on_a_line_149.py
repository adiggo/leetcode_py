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
