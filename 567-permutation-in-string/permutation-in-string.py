class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        s2_length = len(s2)
        pointer_left = 0
        pointer_right = s1_length - 1
        s1_arr = [0] * 26
        s2_arr = [0] * 26

        if s2_length < s1_length:
            return False

        for char in s1:
            s1_arr[ord(char) - ord('a')] += 1

        for i in range(pointer_left, pointer_right):
            if s2[i] in s1:
                s2_arr[ord(s2[i]) - ord('a')] += 1

        while pointer_right < s2_length:
            if s2[pointer_right] in s1:
                s2_arr[ord(s2[pointer_right]) - ord('a')] += 1
            if (self.equalArrays(s1_arr, s2_arr)):
                return True   
            if s2_arr[ord(s2[pointer_left]) - ord('a')] > 0: 
                s2_arr[ord(s2[pointer_left]) - ord('a')] -= 1         

            pointer_left += 1
            pointer_right += 1
        return False


    def equalArrays(self, arr1, arr2):
        for i in range(26):
            if arr1[i] != arr2[i]:
                return False
        return True