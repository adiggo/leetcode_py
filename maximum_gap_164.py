class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums or len(nums) < 2:
            return 0
        nums.sort()
        prev = nums[0]
        res = 0
        for i in nums[1:]:
            res = max(abs(i - prev), res)
            prev = i
        return res


# radix sort
    def maximumGap2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 2:
            return 0
        # radix sort
        # for each digit, do counting sort
        strNums = []
        maxSize = 0
        for num in nums:
            strNum = str(num)[::-1]
            maxSize = max(maxSize, len(strNum))
            strNums.append(strNum)
        # radix sort
        for i in xrange(maxSize):
            buckets = [[] for x in xrange(10)]
            for strNum in strNums:
                if len(strNum) <= i:
                    buckets[0].append(strNum)
                else:
                    buckets[int(strNum[i])].append(strNum)
            strNums = []
            for i in xrange(10):
                strNums.extend(buckets[i])
        # reverse back nums
        curNums = [int(x[::-1]) for x in strNums]
        res = 0
        for i in xrange(1, len(curNums)):
            res = max(curNums[i] - curNums[i-1], res)
        return res
                
#reference: https://leetcode.com/discuss/18543/memory-limit-exceeded-my-python-code-got-a-mle        
#bucket sort
    def maximumGap3(self, num):
        l = len(num)
        if l < 2:
            return 0
        min_num = min(num)
        max_num = max(num)
        # max gap must be larger or equal to bucketRange
        bucketRange = max(1, int((max_num - min_num - 1) / (l-1)) + 1) #ceil( (max_num - min_num) / (l - 1) )
        # number of buckets
        bucketNum = (max_num - min_num) / bucketRange + 1
        buckets = [None] * bucketNum
        for n in num:
            loc = (n - min_num) / bucketRange
            bucket = buckets[loc]
            if bucket is None:
                bucket = {'min' : n, 'max' : n}
                buckets[loc] = bucket
            else:
                bucket['min'] = min(bucket['min'], n)
                bucket['max'] = max(bucket['max'], n)
        maxGap = 0
        for x in range(bucketNum):
            if buckets[x] is None:
                continue
            y = x + 1
            # skip the empty buckets
            while y < bucketNum and buckets[y] is None:
                y += 1
            if y < bucketNum:
                maxGap = max(maxGap, buckets[y]['min'] - buckets[x]['max'])
            x = y
        return maxGap        
