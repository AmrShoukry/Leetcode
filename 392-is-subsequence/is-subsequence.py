class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer_t = 0
        pointer_s = 0
        len_t = len(t)
        len_s = len(s)

        while (pointer_s < len_s):
            if pointer_t >= len_t:
                return False
            for i in range(pointer_t, len_t):
                if t[pointer_t] == s[pointer_s]:
                    pointer_t += 1
                    pointer_s += 1
                    break
                else:
                    pointer_t += 1 
        return True

            