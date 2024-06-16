class TrieNode:
    def __init__(self) -> None:
        self.children=[None]*26
        self.isEndOfWord=False
        

class Tries:
    def __init__(self) -> None:
        self.root=TrieNode()
        # print('Root',self.root)
    
    def _charToIndex(self,char):
        return ord(char)-ord('a')
    
    def insert(self,character):
        node=self.root
        length=len(character)
        for i in range(length):
            index=ord(character[i])-ord('a')
            if not node.children[index]:
                node.children[index]=TrieNode()
            node=node.children[index]
        node.isEndOfWord=True

    def search(self,character):
        root=self.root
        lenght=len(character)
        for i in range(lenght):
            index=ord(character[i])-ord('a')   
            if not root.children[index]:
                return False
            root=root.children[index]
        return root.isEndOfWord

    def display(self,character):
        val=self.search(character)
        if val is True:
            print('Present in Trie.') 
        else:
            print('Not Present in Trie.')

Trie=Tries()
characters=['arun','kumar','shivam','shreya']
for i in characters:
    Trie.insert(i)

print(Trie.search('kumar'))
print(Trie.search('kunal'))
Trie.display('kumar')
Trie.display('shreya')
Trie.display('kunal')