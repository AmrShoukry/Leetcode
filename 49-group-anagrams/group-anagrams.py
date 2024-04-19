class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        array = []
        index = 0
        for string in strs:
            sorted_string = ''.join(sorted(string))
            print(sorted_string)
            try:
                stored_index = anagrams[sorted_string]
                array[stored_index].append(string)
            except:
                anagrams[sorted_string] = index
                array.append([string])
                index += 1
        return array
        