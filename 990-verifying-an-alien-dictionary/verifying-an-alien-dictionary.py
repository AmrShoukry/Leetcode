class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letters = {}
        wordsLength = len(words)
        for index, letter in enumerate(order):
            letters[letter] = index
        for i in range(1, wordsLength):
            word1Length = len(words[i - 1])
            word2Length = len(words[i])
            word1Pointer = 0
            word2Pointer = 0
            while word1Pointer < word1Length and word2Pointer < word2Length:
                if letters[words[i - 1][word1Pointer]] > letters[words[i][word2Pointer]]:
                    return False
                elif letters[words[i - 1][word1Pointer]] < letters[words[i][word2Pointer]]:
                    break
                word1Pointer += 1
                word2Pointer += 1
            if word1Pointer < word1Length and word2Pointer >= word2Length:
                return False
        return True
