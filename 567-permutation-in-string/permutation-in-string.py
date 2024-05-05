class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        s2_length = len(s2)
        pointer_left = 0
        pointer_right = s1_length - 1

        while pointer_right < s2_length:
            found = True
            s1_hash = {}
            for char in s1:
                value = s1_hash.get(char, 's')
                if value == 's':
                    s1_hash[char] = 1
                else:
                    s1_hash[char] += 1
            for i in range(pointer_left, pointer_right + 1):
                value = s1_hash.get(s2[i], 's')
                if value != 's':
                    s1_hash[s2[i]] -= 1
            for item in s1_hash:
                if s1_hash[item] != 0:
                    found = False
                    break
            if found:
                return True
            
            pointer_left += 1
            pointer_right += 1
        return False
