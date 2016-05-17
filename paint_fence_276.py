def get_total_paint(n, k):
    # n posts, k colors
    if k <= 0:
        return 0
    first = k
    second = k * k
    if k < 3:
        return first if k == 1 else return second
    for i in xrange(3, n + 1):
        third = (k-1) * first + (k-1) * second
        first = second
        second = third
    return third
