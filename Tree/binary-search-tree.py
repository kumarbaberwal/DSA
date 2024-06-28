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

    def delete(self, data):
        if self.root:
            self.root = self._delete(self.root, data)
        else:
            print('Binary Search Tree is Empty!')
    
    def _delete(self, node, data):
        if not node:
            return None
        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            node.data = self._minValueNode(node.right)
            node.right = self._delete(node.right, node.data)
        return node

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
    
    def postorderTraversal(self):
        return self._postorderTraversal(self.root) if self.root else print('Binary Search Tree is Empty')
    
    def _postorderTraversal(self, node):
        if node:
            self._postorderTraversal(node.left)
            self._postorderTraversal(node.right)
            print(node.data)

    def findMin(self):
        return self._minValueNode(self.root) if self.root else print('Binary Search Tree is Empty')
    
    def _minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        print(f'Minimum Value : {current.data}')
        return current.data

    def findMax(self):
        return self._maxValueNode(self.root) if self.root else print('Binary Search Tree is Empty')
    
    def _maxValueNode(self, node):
        current = node
        while current.right:
            current = current.right
        print(f'Maximum Value : {current.data}')

    def height(self):
        if self.root:
            return print(f'The height of Binary Search Tree is: {self._height(self.root)}')
        else:
            print('Binary Search Tree is Empty')
    
    def _height(self, node):
        if not node:
            return 0
        else:
            leftHeight = self._height(node.left)
            rightHeight = self._height(node.right)
            return max(leftHeight, rightHeight) + 1

if __name__ == "__main__":
    bst = BinarySeachTree()
    # bst.inorderTraversal()
    bst.insert(9)
    bst.insert(10)
    bst.insert(8)
    bst.insert(11)
    bst.inorderTraversal()
    print()
    bst.search(8)
    print()
    bst.search(9)
    print()
    bst.search(10)
    print()
    bst.search(11)
    print()
    bst.search(12)
    print()
    bst.findMin()
    print()
    bst.findMax()
    print()
    bst.preorderTraversal()
    print()
    bst.postorderTraversal()
    print()
    bst.height()
    print()
    bst.delete(8)
    bst.inorderTraversal()
    print()
    bst.delete(9)
    bst.inorderTraversal()