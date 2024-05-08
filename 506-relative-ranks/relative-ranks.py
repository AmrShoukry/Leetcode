class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        length = len(score)
        sorted_arr = sorted(score, reverse=True)
        rank = [-1] * length
        hashes = {}
        for i in range(length):
            hashes[sorted_arr[i]] = i + 1

        for i in range(length):
            value = hashes[score[i]]  
            if value == 1:
                value = 'Gold Medal'
            elif value == 2:
                value = 'Silver Medal'
            elif value == 3:
                value = 'Bronze Medal'
            else:
                value = f"{value}"
            rank[i] = value      

        return rank


