class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.isEndOfWord = False

class Tries:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word.lower():
            if 'a' <= char <= 'z':
                index = ord(char) - ord('a')
                if not current_node.children[index]:
                    current_node.children[index] = TrieNode()
                current_node = current_node.children[index]
        current_node.isEndOfWord = True
    
    def search(self, word):
        if self._search(word):
            print(f'{word} is Present in Tries')
        else:
            print(f'{word} is not Present in Tries')

    def _search(self, word):
        current_node = self.root
        for char in word:
            if 'a' <= char <= 'z':
                index = ord(char) - ord('a')
                if not current_node.children[index]:
                    return False
                current_node = current_node.children[index]
        return current_node.isEndOfWord
    
if __name__ == '__main__':
    tries = Tries()
    Words = ['kumar', 'rohan', 'isha', 'mehak', 'rohit']
    for i in Words:
        tries.insert(i)

    tries.search('kumar')
    tries.search('mehak')
    tries.search('isha')