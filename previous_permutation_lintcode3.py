class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def previousPermuation(self, num):
        # write your code here
        if num is None:
            return None
        ascending = True
        res = []
        for i in range(len(num)-1, 0, -1):
            if num[i] >= num[i-1]:
                res.append(num[i])
                continue
            if num[i] < num[i-1]:
                num[i-1], num[i] = num[i], num[i-1]
                # get the index
                index = self.bst(res, num[i])
                if index >= len(res) or (index == len(res)-1 and res[index] == num[i]):
                    res.append(num[i])
                    res = num[0: i] + res
                else:
                    replace_val = res[index]
                    if replace_val == num[i]:
                        index += 1
                        replace_val = res[index]
                    res[index] = num[i]
                    res.append(num[i-1])
                    res = num[0: i-1] +[replace_val]+ res
                ascending = False
                break
        if not ascending:
            return res
        else:
            return num[::-1]
    
    # bst a descending list
    def bst(self, nums, num):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left)/2
            if nums[mid] > num:
                left = mid + 1
            elif nums[mid] < num:
                right = mid - 1
            else:
                return mid
        return left
