class TreeNode:
    def __init__(self, data) -> None:
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self) -> None:
        self.root=None

    def insert(self, data):
        if self.root is None:
            self.root=TreeNode(data)
            return
        else: 
            self.recursivelyinsert(self.root,TreeNode(data))
                
    def recursivelyinsert(self, node, newnode):
        if newnode.data<node.data:
            if node.left is None:
                node.left=newnode
                return
            else:
                self.recursivelyinsert(node.left,newnode)
        else:
            if node.right is None:
                node.right=newnode
                return
            else:
                self.recursivelyinsert(node.right,newnode)


    def inorder(self):
        self._inorder(self.root)

    def _inorder(self,node):
        root=self.root
        if root is None:
            print("Binary Tree is Empty.")
            return
        else:
            if node is not None:
                self._inorder(node.left)
                print(node.data)
                self._inorder(node.right)

bt=BinaryTree()
bt.insert(7)
bt.insert(4)
bt.insert(1)
bt.insert(9)
bt.inorder()