# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder curr left right
        # inorder left curr right

        inorderDict = {}
        for i in range(len(inorder)):
            inorderDict[inorder[i]] = i

        preIndex = 0

        def helper(low, high):
            nonlocal preIndex

            if low > high:
                return None
            
            inorderIndex = inorderDict[preorder[preIndex]]

            node = TreeNode(preorder[preIndex])
            preIndex += 1

            node.left = helper(low, inorderIndex - 1)
            node.right = helper(inorderIndex + 1, high)
            return node

        return helper(0, len(preorder) - 1)