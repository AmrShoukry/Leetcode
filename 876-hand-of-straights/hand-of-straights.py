class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        length = len(hand)
        if length % groupSize != 0:
            return False

        nums = sorted(hand)
        rows = {}
        iterations = {}
        groups = length // groupSize

        for i in range(groups):
            rows[i] = 's'
            iterations[i] = 0
        
        for num in nums:
            found = 0
            for key, value in rows.items():
                if value == 's' or (num == rows[key] + 1 and iterations[key] < groupSize):
                    rows[key] = num
                    iterations[key] += 1
                    found = 1
                    break
            if found == 0:
                return False

        return True


