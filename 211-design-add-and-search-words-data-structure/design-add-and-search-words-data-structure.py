class WordDictionary:

    def __init__(self):
        self.hashes = {}

    def addWord(self, word: str) -> None:
        current_hash = self.hashes
        for char in word:
            if char not in current_hash.keys():
                current_hash[char] = {}
            current_hash = current_hash[char]
        current_hash['end'] = True

    def search(self, word: str) -> bool:
        return self.search_helper(word, self.hashes)

    def search_helper(self, word, inner_hash):
        if not word:
            return 'end' in inner_hash
        char = word[0]
        if char == '.':
            for key in inner_hash:
                if key != 'end' and self.search_helper(word[1:], inner_hash[key]):
                    return True
        elif char in inner_hash:
            return self.search_helper(word[1:], inner_hash[char])
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)