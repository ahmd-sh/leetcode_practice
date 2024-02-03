# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        node = root

        tmp = node.left
        node.left = node.right
        node.right = tmp

        if node.left:
            self.invertTree(node.left)

        if node.right:
            self.invertTree(node.right)

        return root


# # More concise code: 
# tmp = root.left
# root.left = root.right
# root.right = tmp
# self.invertTree(root.left)
# self.invertTree(root.right)
