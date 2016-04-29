class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def verticalTraversal(self, root):
        if not root:
            return []
        map = dict()
        self.dfs(root, 0, map)
        res = []
        # it is continuous
        # get the range
        min_vertical, max_vertical = None, None
        for key in map:
            min_vertical = min(min_vertical, key) if min_vertical is not None else key
            max_vertical = max(max_vertical, key) if max_vertical is not None else key

        while min_vertical <= max_vertical:
            res.append(map.get(min_vertical))
            min_vertical += 1
        return res

    # use a vertical level to record current vertical position
    def dfs(self, root, vertical_level, map):
        if not root:
            return
        if vertical_level in map:
            map.get(vertical_level).append(root.val)
        else:
            map[vertical_level] = [root.val]
        self.dfs(root.left, vertical_level - 1, map)
        self.dfs(root.right, vertical_level + 1, map)
