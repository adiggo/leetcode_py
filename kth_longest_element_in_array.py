class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        # so in the first time, it will never equal
        i = len(nums)
        left = 0
        right = len(nums) - 1
        index = len(nums) - k
        # the order of kth element is n-k index in the sorted array
        while i != index:
            pivot = nums[left]
            #keep record of left and right
            leftindex = left+1
            rightindex = right
            while (leftindex <= rightindex):
                if nums[leftindex] <= pivot:
                    leftindex += 1
                else:
                    nums[leftindex], nums[rightindex] = nums[rightindex], nums[leftindex]
                if nums[rightindex] > pivot:
                    rightindex -= 1
                else:
                    if leftindex < len(nums) and leftindex <= rightindex:
                        nums[rightindex], nums[leftindex] = nums[leftindex], nums[rightindex]
            i = rightindex
            #swap the pivot to corresponding place
            nums[left], nums[rightindex] = nums[rightindex], nums[left]
            if rightindex < index:
                left = rightindex + 1
                # keep right not change
            elif rightindex > index:
                right = rightindex - 1
            else:
                return nums[rightindex]
        # i is the kth largest number
        return nums[i]
