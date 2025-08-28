# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        res = []
        def inorder(root, res):
            if not root:
                return res
            res = inorder(root.left, res)
            res.append(root.val)
            res = inorder(root.right, res)
            return res
        
        return(inorder(root, res))


root = TreeNode(2, TreeNode(1), TreeNode(3))

print(Solution().inorderTraversal(root))
