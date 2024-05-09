class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness = sorted(happiness, reverse=True)
        length = len(happiness)
        counter = 0

        for i in range(k):
            counter += happiness[i]
            if i + 1 < length:
                if happiness[i + 1] - (i + 1) >= 0:
                    happiness[i + 1] -= (i + 1)
                else:
                    happiness[i + 1] = 0

        return counter
