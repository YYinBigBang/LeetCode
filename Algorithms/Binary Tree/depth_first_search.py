# Depth First Search (DFS) algorithm

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeTraversal:
    def __init__(self, root):
        self.root = root

    def pre_order_recursive(self, node):
        if not node:
            return
        print(node.val, end=" ")
        self.pre_order_recursive(node.left)
        self.pre_order_recursive(node.right)

    def pre_order_iterative(self):
        if not self.root:
            return
        stack = [self.root]
        while stack:
            current = stack.pop()
            print(current.val, end=" ")
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    def in_order_recursive(self, node):
        if not node:
            return
        self.in_order_recursive(node.left)
        print(node.val, end=" ")
        self.in_order_recursive(node.right)

    def in_order_iterative(self):
        stack = []
        current = self.root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            print(current.val, end=" ")
            current = current.right

    def post_order_recursive(self, node):
        if not node:
            return
        self.post_order_recursive(node.left)
        self.post_order_recursive(node.right)
        print(node.val, end=" ")

    def post_order_iterative(self):
        if not self.root:
            return
        stack1 = [self.root]
        stack2 = []
        while stack1:
            current = stack1.pop()
            stack2.append(current)
            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)
        while stack2:
            print(stack2.pop().val, end=" ")


# Construct a binary tree:
#        1
#       / \
#      2   3
#     / \
#    4   5
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3)

# instantiate the class
tree_traversal = BinaryTreeTraversal(root)

print("Pre-order Recursive:")
tree_traversal.pre_order_recursive(tree_traversal.root)  # output: 1 2 4 5 3

print("\nPre-order Iterative:")
tree_traversal.pre_order_iterative()  # output: 1 2 4 5 3

print("\nIn-order Recursive:")
tree_traversal.in_order_recursive(tree_traversal.root)  # output: 4 2 5 1 3

print("\nIn-order Iterative:")
tree_traversal.in_order_iterative()  # output: 4 2 5 1 3

print("\nPost-order Recursive:")
tree_traversal.post_order_recursive(tree_traversal.root)  # output: 4 5 2 3 1

print("\nPost-order Iterative:")
tree_traversal.post_order_iterative()  # output: 4 5 2 3 1
print("\n")

