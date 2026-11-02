# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # return the kth smallest in the three
        # 1 index
        # successor counting? go all the way left, then check parent right then parent for the next left
        stack = [root]
        curr = root
        count = 1

        while stack:
            while curr.left:
                curr = curr.left
                stack.append(curr)
            
            node = stack.pop()
            if count == k:
                return node.val

            if node.right:
                curr = node.right
                stack.append(curr)
            
            count += 1