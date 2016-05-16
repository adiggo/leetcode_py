class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # find the first v larger equal than n - i
        l = len(citations)
        left, right = 0, l-1
        while right >= left:
            mid = left + (right-left)/2
            if citations[mid] >= l-mid:
                right = mid - 1
            elif citations[mid] < l-mid:
                left = mid + 1
        return l - left


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # find the first v larger equal than n - i
        l = len(citations)
        left, right = 0, l-1
        while right >= left:
            mid = left + (right-left)/2
            if citations[mid] == l-mid:
                left = mid
                break
            if citations[mid] > l-mid:
                right = mid - 1
            elif citations[mid] < l-mid:
                left = mid + 1
        return l - left
