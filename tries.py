class TrieNode:
    def __init__(self) -> None:
        self.children=[None]*26
        self.isEndOfWord=False
        

class Tries:
    def __init__(self) -> None:
        self.root=self.getNode()
        print('Root',self.root)

    def getNode(self):
        return TrieNode()


Trie=Tries()