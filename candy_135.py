class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        length = len(ratings)
        candies = [1] * length
        for i in range(length-1):
            diff = ratings[i+1] - ratings[i]
            # if increase
            if diff > 0:
                candies[i+1] = candies[i] + 1
                
        for i in range(length-1, 0, -1):
            diff = ratings[i] - ratings[i-1]
            if diff < 0:
                # use the higher value of candies[i]+1 or candies[i-1]
                # [4,2,3,4,1]   --> candies[3] = 2 if we don't apply max, actually it should be equal to 3.
                # only change candies[i-1] when candies[i] + 1 is larger than candies[i-1]
                candies[i-1] = max(candies[i] + 1, candies[i-1])
        return sum(candies)
            
