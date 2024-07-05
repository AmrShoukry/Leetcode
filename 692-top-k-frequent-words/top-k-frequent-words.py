class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        length = len(words)
        iterations = {}
        array = [-1] * (length + 1)
        solution = []
        for word in words:
            iterations[word] = iterations.get(word, 0) + 1
        for key, value in iterations.items():
            if array[value] == -1:
                array[value] = [key]
            else:
                array[value].append(key)
                array[value] = sorted(array[value])
        for i in range(length, -1, -1):
            if array[i] == -1:
                continue
            while array[i]:
                solution.append(array[i].pop(0))
                k -= 1
                if k == 0:
                    return solution

        
