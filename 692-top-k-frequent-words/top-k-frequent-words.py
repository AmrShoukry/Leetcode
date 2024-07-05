class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        length = len(words)
        iterations = {}
        solution = []
        for word in words:
            iterations[word] = iterations.get(word, 0) + 1
        
        heap = []

        for word, freq in iterations.items():
            heapq.heappush(heap, (-freq, word))
        
        for i in range(k):
            solution.append(heapq.heappop(heap)[1])

        return solution
