# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        queue = deque([(root, 0)])
        answer = []

        while queue:
            # Pop the first element from the queue
            node, depth = queue.popleft()
            if node:
                if len(answer) <= depth:
                    answer.append([])

                # Append the value of the node to the list at the current depth
                answer[depth].append(node.val)

                # Add the left and right children of the current node to the queue
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))

        return answer

