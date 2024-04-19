class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        array = []
        index = 0
        for string in strs:
            char_array = [0] * 26
            for char in string:
                char_array[ord(char) - 97] += 1
            try:
                stored_index = anagrams[f"'{char_array}'"]
                array[stored_index].append(string)
            except:
                anagrams[f"'{char_array}'"] = index
                array.append([string])
                index += 1
        return array
        