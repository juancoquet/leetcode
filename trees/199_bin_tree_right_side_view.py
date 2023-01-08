# https://leetcode.com/problems/binary-tree-right-side-view/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traverse(root, depth=1):
            if not root:
                return
            if len(res) < depth:
                res.append(root.val)
            traverse(root.right, depth + 1)
            traverse(root.left, depth + 1)

        traverse(root)
        return res
