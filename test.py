class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursively(self.root, TreeNode(data))

    def _insert_recursively(self, node, new_node):
        if new_node.data < node.data:
            if not node.left:
                node.left = new_node
            else:
                self._insert_recursively(node.left, new_node)
        else:
            if not node.right:
                node.right = new_node
            else:
                self._insert_recursively(node.right, new_node)

    def display(self, node):
        if node is not None:
            self.display(node.left)
            print(node.data)
            self.display(node.right)

bt = BinaryTree()
bt.insert(4)
bt.insert(9)
bt.insert(2)
bt.insert(7)
bt.insert(1)

bt.display(bt.root)
