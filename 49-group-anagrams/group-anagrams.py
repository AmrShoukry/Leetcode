class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        solution = []
        index = 0
        for string in strs:
            sortedStr = ''.join(sorted(string))

            val = anagrams.get(sortedStr, -1)
            if val == -1:
                solution.append([string])
                anagrams[sortedStr] = index
                index += 1
            else:
                solution[val].append(string)
        return solution

        