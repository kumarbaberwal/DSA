class TreeNode:
    def __init__(self, data) -> None:
        self.data=data
        self.right=None
        self.left=None
        self.height=1

class AVL:
    def  __init__(self) -> None:
        self.root=None