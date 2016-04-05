class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = (len(nums)-1)/2
        left = self.sortedArrayToBST(nums[:mid])
        right = self.sortedArrayToBST(nums[mid+1:])
        root = TreeNode(nums[mid])
        root.left = left
        root.right = right
        return root
