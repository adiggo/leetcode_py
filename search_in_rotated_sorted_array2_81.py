class Solution(object):
    def search(self, nums, target):
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return True
            # sorted right half
            if nums[mid] < nums[end]:
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            # left half is sorted
            elif nums[mid] > nums[end]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                end -= 1
        return False

