class Solution(object):
    def cost(costs):
        if not costs:
            return 0
        r, b, g = 0, 0, 0
        for cost in costs:
            rr, bb, gg = r, b, g
            r = cost[0] + min(bb, gg)
            b = cost[1] + min(rr, gg)
            g = cost[2] + min(rr, bb)
        return min(r, b, g)
