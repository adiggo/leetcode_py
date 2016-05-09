
# reference: http://www.cnblogs.com/AnnieKim/archive/2013/06/15/MorrisTraversal.html
def inorder_morris(root):
    cur, prev = root, None
    res = []
    while cur:
        if not cur.left:
            res.append(cur.val)
            cur = cur.right
        else:
            prev = cur.left
            while prev.right and prev.right != cur:
                prev = prev.right
            # if predecessor.right is None, which means the predecessor is not visited yet
            if not prev.right:
                prev.right = cur
                cur = cur.left
            else:
                #predecessor just visited, delete the predecessor relationship
                prev.right = None
                res.append(cur.val)
                cur = cur.right
    return res

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

