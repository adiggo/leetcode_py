class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        l1, l2 = len(v1), len(v2)
        
        
        for i in range(max(l1, l2)):
            ver1 = int(v1[i]) if i < len(v1) else 0
            ver2 = int(v2[i]) if i < len(v2) else 0
            if ver1 > ver2:
                return 1
            elif ver1 < ver2:
                return -1
        return 0
            
