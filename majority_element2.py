class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        # the minimum elements for the requirement is > n/3
        candidate1, candidate2, c1, c2 = None, None, 0, 0
        
        for num in nums:
            if num == candidate1:
                c1 += 1
            elif num == candidate2:
                c2 += 1
            elif c1 == 0:
                c1 = 1
                candidate1 = num
            elif c2 == 0:
                c2 = 1
                candidate2 = num
            else:
                c1 -= 1
                c2 -= 1
        
        return [n for n in [candidate1, candidate2] if n is not None and nums.count(n) > len(nums)/3]
