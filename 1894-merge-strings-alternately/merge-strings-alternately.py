class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_word1 = len(word1)
        len_word2 = len(word2)
        pointer1 = 0
        pointer2 = 0
        string = ""

        while (pointer1 < len_word1 and pointer2 < len_word2):
            string += word1[pointer1]
            string += word2[pointer2]
            pointer1 += 1
            pointer2 += 1
        while (pointer1 < len_word1):
            string += word1[pointer1]
            pointer1 += 1
        while (pointer2 < len_word2):
            string += word2[pointer2]
            pointer2 += 1
        return string