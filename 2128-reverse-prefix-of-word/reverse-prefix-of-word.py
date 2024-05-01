class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        right_pointer = -1
        left_pointer = 0
        temp = 0
        final_word = ""
        length = len(word)

        for i in range(length):
            if word[i] == ch:
                right_pointer = i
                break
        
        if right_pointer == -1:
            return word

        temp = right_pointer + 1
        while(left_pointer <= right_pointer):
            final_word += word[right_pointer]
            right_pointer -= 1

        while(temp < length):
            final_word += word[temp]
            temp += 1

        return final_word

            