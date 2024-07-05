class Node:
    def __init__(self):
        self.children = {}
        self.done = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root

        for char in word:
            node = current.children.get(char, -1)
            if node == -1:
                node = Node()
                current.children[char] = node
            current = node
        current.done = True

    def search(self, word: str) -> bool:
        current = self.root

        for char in word:
            node = current.children.get(char, -1)
            if node == -1:
                return False
            current = node
        return current.done
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for char in prefix:
            node = current.children.get(char, -1)
            if node == -1:
                return False
            current = node
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)