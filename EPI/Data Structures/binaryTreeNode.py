class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def treeTraversal(node):
        if node:
            # Preorder: process root before traversal of left and right children
            print('Preorder: %d' % node.data
            tree_traversal(node.left)
            # Inorder: processes root after traversal of left and before traversal of right
            print('Inorder: %d' % node.data)
            tree_traversal(node.right)
            # Postorder: Process root after traversal of lef  t and right
            print('Postorder: %d' % node.data)

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
