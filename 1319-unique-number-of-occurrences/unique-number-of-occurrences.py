class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        length = len(arr)
        occurences = {}
        nums = ['s'] * (length + 1)
        for num in arr:
            count = occurences.get(num, 0)
            if count == 0:
                occurences[num] = 1
            else:
                occurences[num] += 1

        for key, value in occurences.items():
            if nums[value] != 's':
                return False
            nums[value] = key
        return True 