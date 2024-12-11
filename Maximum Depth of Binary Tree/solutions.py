# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0

        left_path = self.maxDepth(root.left)
        right_path = self.maxDepth(root.right)

        if left_path > right_path:
            return left_path + 1
        else:
            return right_path + 1


class Solution2(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0

        stack = [(root, 1)]
        max_depth = 0

        while stack:
            node, depth = stack.pop()

            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return max_depth

