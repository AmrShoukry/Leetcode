class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        length = len(hand)
        if length % groupSize != 0:
            return False
        
        iterations = {}

        for num in hand:
            iterations[num] = iterations.get(num, 0) + 1
        
        heap = list(iterations.keys())
        heapq.heapify(heap)

        while heap:
            least = heap[0]

            for i in range(least, least + groupSize):
                if i not in iterations:
                    return False
                iterations[i] -= 1
                if iterations[i] == 0:
                    if heap[0] != i:
                        return False
                    heapq.heappop(heap)
        return True