# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # check if both nodes are None
        if p is None and q is None:
            return True

        # check if one of the nodes is None
        if p is None or q is None:
            return False

        # check if the values of the nodes are different
        if p.val != q.val:
            return False

        # recursively check the left and right subtree
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class solution2(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        stack = [(p, q)]

        while stack:
            node1, node2 = stack.pop()

            if not node1 and not node2:
                continue

            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False

            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))

        return True

