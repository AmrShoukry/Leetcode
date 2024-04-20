class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        iterations = {}
        values = []
        for num in nums:
            iterations[num] = iterations.get(num, 0) + 1
        
        for i in range(k):
            maximum_value = -1
            maximum_key = -1
            for [key, value] in iterations.items():
                if (value > maximum_value):
                    maximum_value = value
                    maximum_key = key
            iterations[maximum_key] = -1
            values.append(maximum_key)
        
        return values