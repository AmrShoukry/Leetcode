class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        iterations = {}
        array_length = len(nums)
        array = ['s'] * (array_length + 1)
        found = 0
        solution = []
        for num in nums:
            iterations[num] = iterations.get(num, 0) + 1
        for [key, value] in iterations.items():
            if array[value] == 's':
                array[value] = [key]
            else:
                array[value].append(key)
        for i in range(array_length, -1 , -1):
            for element in array[i]:
                if (element != 's'):
                    solution.append(element)
                    found += 1
                    if found == k:
                        return solution
