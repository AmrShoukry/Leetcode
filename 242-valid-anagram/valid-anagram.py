class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for letter in s:
            letters[letter] = letters.get(letter, 0) + 1
        for letter in t:
            remaining = letters.get(letter, 0)
            if remaining < 1:
                return False
            letters[letter] -= 1
        for key, value in letters.items():
            if value != 0:
                return False
        return True
        