class TrieNode:
    def __init__(self) -> None:
        self.children=[None]*26
        self.isEndOfWord=False

class Trie:
    def __init__(self) -> None:
        self.root=TrieNode()
    
    def insert(self,character):
        node=self.root
        lenght=len(character)
        for i in range(lenght):
            index=ord(character[i])-ord('a')
            if not node.children[index]:
                node.children[index]=TrieNode()
            node=node.children[index]
        node.isEndOfWord=True
    
    def search(self,character):
        node=self.root
        length=len(character)
        for i in range(length):
            index=ord(character[i])-ord('a')
            if not node.children[index]:
                return False
            node=node.children[index]
        return node.isEndOfWord
    
trie=Trie()
trie.insert('kumar')
trie.insert('shivam')
trie.insert('kumal')
print(trie.search('kumal'))
print(trie.search('kuma'))
print(trie.search('shiv'))
print(trie.search('shivam'))