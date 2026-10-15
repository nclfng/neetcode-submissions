# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []

        if not root:
            return []

        # add to list
            # look at level, if output len > lvl, row already exists so add to it
            # else make it
        
        def helper(root, level):
            if not root:
                return
            
            if len(output) > level:
                output[level].append(root.val)
            else:
                output.append([root.val])
            
            helper(root.left, level + 1)
            helper(root.right, level + 1)
            return output
        
        # check left and right
        return helper(root, 0)