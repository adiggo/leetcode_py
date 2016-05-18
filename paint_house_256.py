def cost(costs):
    if not costs:
        return 0
    r, b, g = 0, 0, 0
    for cost in costs:
        rr, bb, gg = r, b, g
        r = rr + min(cost[1], cost[2])
        b = bb + min(cost[0], cost[2])
        g = gg + min(cost[0], cost[1])
    return min(r, b, g)
