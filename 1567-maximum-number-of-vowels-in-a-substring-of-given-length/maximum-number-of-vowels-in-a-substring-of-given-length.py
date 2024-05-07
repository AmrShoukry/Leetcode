class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        pointer_left = 0
        pointer_right = k - 1
        length = len(s)
        vowels_count = 0

        for i in range(pointer_left, pointer_right + 1):
            if s[i] in vowels:
                vowels_count += 1
        maximum_length = vowels_count

        if s[pointer_left] in vowels:
            vowels_count -= 1

        pointer_left += 1
        pointer_right += 1

        while pointer_right < length:
            if s[pointer_right] in vowels:
                vowels_count += 1
            maximum_length = max(maximum_length, vowels_count)
            if s[pointer_left] in vowels:
                vowels_count -= 1

            pointer_left += 1
            pointer_right += 1
    
        return maximum_length


     
        