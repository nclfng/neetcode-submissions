# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # good = path from root contains all notes <= x
        count = 0

        # traverse through root
        # know the max number for that path?, compare to prev number
        # update curr max
        # add one for root immediately

        def helper(curr, currMax):
            nonlocal count

            if curr is None:
                return
 
            if curr.val >= currMax:
                count += 1
                currMax = curr.val
            
            helper(curr.left, currMax)
            helper(curr.right, currMax)

            return count
        
        return helper(root, root.val)