def missing_range(nums, start, end):
    if not nums:
        raise ValueError('input should not be empty')
    res = []
    if nums[0] > start:
        res.append(getrange(start, nums[0] - 1))
    prev = nums[0]
    for i in xrange(1, len(nums)):
        cur = nums[i]
        if cur - prev <= 1:
            prev = cur
        else:
            res.append(getrange(prev + 1, cur - 1))
            prev = cur

    if prev < end:
        res.append(getrange(prev + 1, end))

    return res


def getrange(l, r):
    if r - l >= 1:
        return str(l) + '->' + str(r)
    else:
        return str(l)
