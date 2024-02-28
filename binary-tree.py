class TreeNode:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None


class BinaryTree:
    def __init__(self) -> None:
        self.root=None

    def Insert(self,data):
        root=TreeNode(data)
        if self.root==None:
            self.root=root
        else:
            self._InsertRecursively(self.root,root)


    def _InsertRecursively(self,node,data):
        if data.data<node.data:
            if node.left==None:
                self.left=data
            else:
                self._InsertRecursively(self.left,data)
        else:
            if node.right==None:
                self.right=data
            else:
                self._InsertRecursively(self.right,data)


    def display(self,node):
        if node is not None:
            self.display(node.left)
            print(node.data)
            self.display(node.right)


bt=BinaryTree()
bt.Insert(4)
bt.Insert(9)
bt.Insert(2)
bt.Insert(7)
bt.Insert(1)

bt.display(bt.root)