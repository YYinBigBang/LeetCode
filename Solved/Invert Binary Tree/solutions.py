# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution1(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return

        # Swap the left and right nodes
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root


class Solution2(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None

        # initialize the stack
        stack = [root]

        while stack:
            node = stack.pop()

            # Swap the left and right nodes
            node.left, node.right = node.right, node.left

            # Add the left and right nodes to the stack
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root
