class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) != len(cost):
            raise ValueError("gas and cost should be same length")
        global_diff = 0
        local_diff = 0
        index = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            global_diff += diff
            local_diff += diff
            if local_diff < 0:
                local_diff = 0
                index = i+1
        if global_diff < 0:
            return -1
        else:
            return index if index < len(gas) else -1
