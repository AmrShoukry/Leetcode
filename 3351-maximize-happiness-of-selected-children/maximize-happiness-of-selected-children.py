class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness = sorted(happiness, reverse=True)
        counter = 0

        for i in range(k):
            if happiness[i] - i >= 0:
                happiness[i] -= i
            else:
                happiness[i] = 0
            counter += happiness[i]

        return counter
