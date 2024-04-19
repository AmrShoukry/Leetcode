class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            char_array = [0] * 26
            for char in string:
                char_array[ord(char) - 97] += 1
            key = anagrams.get(tuple(char_array), 'AmrShoukry')
            if key == 'AmrShoukry':
                anagrams[tuple(char_array)] = [string]
            else:
                anagrams[tuple(char_array)].append(string)
        return list(anagrams.values())
        