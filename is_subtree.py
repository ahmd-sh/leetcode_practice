# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                left = isSameTree(p.left, q.left)
                right = isSameTree(p.right, q.right)
                return left and right
            return False

        if not root:
            return True
        if not subRoot:
            return False
        if isSameTree(root, subRoot):
            return True

        left1 = self.isSubtree(root.left, subRoot)
        right1 = self.isSubtree(root.right, subRoot)
        return left1 or right1
