
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # find the max combination from array with size k
        def get_max_sub_array(nums, k):
            stack , n = [] ,len(nums)
            for i in xrange(n):
                # condition to pop element:
                # 1. stack is not empty 
                # 2. current stack length plus remaining length is larger than k  
                # 3. current number larger than the last value of the stack
                while stack and len(stack) + n - i > k and stack[-1] < nums[i]:
                    stack.pop()
                # append this number is the current stack length is less than the specified size
                if len(stack) < k:
                    stack.append(nums[i])
            return stack
        
        res = [0] * k
        for i in xrange(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            res1 = get_max_sub_array(nums1, i)
            res2 = get_max_sub_array(nums2, k - i)
            # merge
            res = max(res, [max(res1, res2).pop(0) for x in xrange(k)])
        return res
