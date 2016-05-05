class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) -1
        # if the first point in another location other than 0, then nums[left] > nums[right]
        while left <= right:
            mid = left + (right - left)/2
            if nums[left] < nums[mid]:
                if nums[left] < nums[right]:
                    return nums[left]
                else:
                    # not include mid
                    left = mid + 1
            elif nums[left] > nums[mid]:
                if nums[mid] < nums[mid-1]:
                    return nums[mid]
                left = left + 1
                right = mid - 1
            else:
                # left + 1== right or left == right
                return min(nums[left], nums[right])
        return nums[left]
        


class Solution2(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) -1
        # if the first point in another location other than 0, then nums[left] > nums[right]
        while left < right:
            mid = left + (right - left)/2
            # base case, mid == left
            if nums[mid] < nums[right]:
                right = mid
            else:
                # not include mid
                left = mid + 1
        return nums[left]




class Solution3(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        left, right = 0, len(nums) -1
        # if the first point in another location other than 0, then nums[left] > nums[right]
        # if left == right, then we can just output nums[left]
        while left <= right:
            mid = left + (right - left)/2
            # min element in range from start to mid inclusive
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                # min element in range from mid+1 to right
                # not include mid because nums[mid] > nums[right]
                # the only case for equal is that there is one element (which is excluded from while loop)
                left = mid + 1
            else:
                return nums[mid]
                
        return nums[left]
