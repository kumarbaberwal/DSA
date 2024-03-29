class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None


    def insert(self,data):
        if self.data is None:
            self.data=Node(data)

        else:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)

            else :
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)

    def preorder(self,node):
        if node is not None:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)


bt=Node(5)
bt.insert(4)
bt.insert(9)
bt.insert(2)
bt.insert(7)
bt.insert(1)

bt.preorder(bt)
