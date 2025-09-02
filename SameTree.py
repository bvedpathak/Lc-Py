# Given the roots of two binary trees p and q, write a 
# function to check if they are the same or not.
# Two binary trees are considered the same if they are 
# structurally identical, and the nodes have the same value.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        
        if p and not q or q and not p:
            return False
        
        if p.val != q.val:
            return False 
        
        return(self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))


root = TreeNode(2, TreeNode(1), TreeNode(3))

print(Solution().isSameTree(root, root))
