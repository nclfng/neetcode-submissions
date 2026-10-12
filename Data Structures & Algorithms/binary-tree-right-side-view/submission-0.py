# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        output = []

        def helper(curr, level):
            # if its a left whose parent has a right, skip
            # if its a right, add
            if not curr:
                return curr
            
            if level == len(output):
                output.append(curr.val)
            
            helper(curr.right, level + 1)
            helper(curr.left, level + 1)

        helper(root, 0)
        return output

        """
        start with root 1
        look at 2 and 3 -- theres a right 3 so append
        next layer search 2 bc 3 none
        4 has no right so add
        5 has no right so add
        """