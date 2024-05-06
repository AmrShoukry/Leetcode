class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        pointer_left = 0
        pointer_right = 0
        length = len(s)
        max_length = 0

        while pointer_right < length:
            val = chars.get(s[pointer_right], 0)
            if val == 0:
                chars[s[pointer_right]] = 1
                pointer_right += 1
            else:
                max_length = max(max_length, pointer_right - pointer_left)
                chars[s[pointer_left]] -= 1
                pointer_left += 1
        max_length = max(max_length, pointer_right - pointer_left)
        return max_length

        return max_length
        