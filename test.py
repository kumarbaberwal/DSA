class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinarySeachTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if not node.left:
                node.left = TreeNode(data)
            else:
                self._insert(node.left, data)
        else:
            if not node.right:
                node.right = TreeNode(data)
            else:
                self._insert(node.right, data)

    def inorderTraversal(self):
        if self.root:
            self._inorderTraversal(self.root)
        else:
            print('Binary Search Tree is Empty!')
    
    def _inorderTraversal(self, node):
        if node:
            self._inorderTraversal(node.left)
            print(node.data)
            self._inorderTraversal(node.right)


if __name__ == "__main__":
    bst = BinarySeachTree()
    # bst.inorderTraversal()
    bst.insert(9)
    bst.insert(10)
    bst.insert(8)
    bst.insert(11)
    bst.inorderTraversal()