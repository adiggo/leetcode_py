import sys
class solution:
    def max_points(self, points):
        if len(points)==0:
        	return 0
        max = 1
        for i in range(len(points)):
            x = points[i].x
            y = points[i].y
            dict = {}
            dict[1.0*(-sys.maxsize-1)] = 1
            dup = 0
            for j in range(i+1, len(points)):
                if points[j].x == x and points[j].y == y:
                    dup = dup+1
                elif points[j].x == x:
                    slope = sys.maxint
                    if slope in dict:
                        dict[slope] = dict[slope] + 1
                    else:
                        dict[slope] = 2
                else:
                    slope = (points[j].y - y)* 1.0/(points[j].x - x)
                    if slope in dict:
                        dict[slope] = dict[slope]+1
                    else:
                        dict[slope] = 2
            for val in dict.values():
                if val+dup > max:
                    max = val+dup
        return max



