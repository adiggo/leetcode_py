# reference: http://bookshadow.com/weblog/2015/10/26/leetcode-serialize-and-deserialize-binary-tree/
class Codec:
    def serialize(self, root):
        def preorder(node):
            if node:
                vals.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
            else:
                vals.append('#')
        vals = []
        preorder(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def depreorder():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = depreorder()
            node.right = depreorder()
            return node
        vals = iter(data.split())
        return depreorder()
