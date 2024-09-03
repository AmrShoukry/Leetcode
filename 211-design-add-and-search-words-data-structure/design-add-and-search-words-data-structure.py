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
            if 'end' in inner_hash.keys():
                return True
            return False
        char = word[0]
        if word[0] == '.':
            for key, value in inner_hash.items():
                returnedValue = self.search_helper(f'{key}{word[1:]}', inner_hash)
                if (returnedValue == True):
                    return True
            return False
        if word[0] in inner_hash.keys():
            return self.search_helper(word[1:], inner_hash[word[0]])
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)