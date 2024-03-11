# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            right_leg_node = None

            for i in range(len(q)):
                node = q.popleft()
                if node:
                    right_leg_node = node
                    q.append(node.left)
                    q.append(node.right)

            if right_leg_node:
                res.append(right_leg_node.val)

        return res
