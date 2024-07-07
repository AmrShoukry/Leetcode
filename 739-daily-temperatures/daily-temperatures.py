class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        stack = []
        answers = [0] * length
        for index, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                oldIndex = stack.pop()
                answers[oldIndex] = index - oldIndex
            stack.append(index)

        return answers