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

    def search(self, value):
        if self.root:
            self._search(self.root, value)
        else:
            print('Binary Search Tree is Empty')
    
    def _search(self, node, value):
        if not node:
            print(f'{value} is not present in the Binary Search Tree')
        elif node.data == value:
            print(f'{value} is Present in the Binary Search Tree')
        elif value < node.data:
            self._search(node.left, value)
        else:
            self._search(node.right, value)

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

    def preorderTraversal(self):
        if self.root:
            self._preorderTraversal(self.root)
        else:
            print('Binary Search Tree is Empty')

    def _preorderTraversal(self, node):
        if node:
            print(node.data)
            self._preorderTraversal(node.left)
            self._preorderTraversal(node.right)

    def findMin(self):
        return self._minValueNode(self.root) if self.root else print('Binary Search Tree is Empty')
    
    def _minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        print(f'Minimum Value : {current.data}')

    def findMax(self):
        return self._maxValueNode(self.root) if self.root else print('Binary Search Tree is Empty')
    
    def _maxValueNode(self, node):
        current = node
        while current.right:
            current = current.right
        print(f'Maximum Value : {current.data}')

if __name__ == "__main__":
    bst = BinarySeachTree()
    # bst.inorderTraversal()
    bst.insert(9)
    bst.insert(10)
    bst.insert(8)
    bst.insert(11)
    bst.inorderTraversal()
    bst.search(8)
    bst.search(9)
    bst.search(10)
    bst.search(11)
    bst.search(12)
    bst.findMin()
    bst.findMax()
    bst.preorderTraversal()