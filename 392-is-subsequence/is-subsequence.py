class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer_t = 0
        pointer_s = 0
        len_t = len(t)
        len_s = len(s)

        if len_s > len_t:
            return False
        
        while(pointer_s < len_s and pointer_t < len_t):
            if s[pointer_s] == t[pointer_t]:
                pointer_s += 1
            pointer_t += 1
        
        if pointer_s < len_s:
            return False
        return True
            