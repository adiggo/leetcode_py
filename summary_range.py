class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        # decide consective: relationship -1
        res = []
        if nums is None or len(nums) == 0:
            return res

        prev = nums[0]
        starting_value = prev
        ending_value = prev
        for num in nums[1:]:
            if num - prev == 1:
                ending_value =  num
                prev = num
            else:
                # append component into result
                component = ''
                if ending_value - starting_value > 0:
                    component = str(starting_value) + '->' + str(ending_value)
                else:
                    component = str(starting_value)
                res.append(component)
                starting_value = num
                ending_value = num
                prev = num
        component = ''
        if ending_value - starting_value > 0:
            component = str(starting_value) + '->' + str(ending_value)
        else:
            component = str(starting_value)
        res.append(component)
        return res
                
