class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) -1
        # code sucks.....
 
        while left <= right:
            mid = left + (right - left)/2
            if nums[left] < nums[mid]:
                # pivotal in (mid, left], which means nums[right] < nums[left] in all case except start from left.
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid]:
                    if target > nums[left]:
                        right = mid - 1
                    elif target < nums[left]:
                        left = mid + 1
                    else:
                        return left
                else:
                    return mid
            elif nums[left] > nums[mid]:
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    if target < nums[right]:
                        left = mid + 1
                    elif target > nums[right]:
                        right = mid - 1
                    else:
                        return right
                else:
                    return mid
            else:
                # only if there is one element
                if nums[mid] == target:
                    return mid
                if mid + 1 < len(nums):
                    if nums[mid+1] == target:
                        return mid+1
                return -1
        return -1

# seperate this rotated sorted array into two part, for one part it is still sorted.
class Solution2(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) -1 
        while left <= right:
            mid = left + (right - left)/2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
                   
