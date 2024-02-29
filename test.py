class TreeNode:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self) -> None:
        self.root=None


    def insert(self,data):
        if self.root is None:
            self.root=TreeNode(data)
            return
        else:
            self.insertrecursively(self.root,TreeNode(data))

    def insertrecursively(self,node,newnode):
        if newnode.data < node.data:
            if node.left is None:
                node.left=newnode
            else:
                self.insertrecursively(node.left,newnode)
        else:
            if node.right is None:
                node.right=newnode
            else:
                self.insertrecursively(node.right,newnode)

    def display(self,node):
        if node is not None:
            self.display(node.left)
            print(node.data)
            self.display(node.right)

bt=BinaryTree()

bt.insert(4)
bt.insert(9)
bt.insert(7)
bt.insert(1)

bt.display(bt.root)