# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def helper(curr, low, high):
            if not curr:
                return True
            
            if not (curr.val > low and curr.val < high):
                return False
            
            return helper(curr.left, low, curr.val) and helper(curr.right, curr.val, high)
        
        return helper(root, float("-inf"), float("inf"))