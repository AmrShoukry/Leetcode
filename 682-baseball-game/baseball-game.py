class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0

        for operation in operations:
            try:
                value = int(operation)
                stack.append(value)
                total += value
            except Exception:
                if operation == 'C':
                    value = stack.pop()
                    total -= value
                elif operation == 'D':
                    value = stack[-1] * 2
                    stack.append(value)
                    total += value
                elif operation == '+':
                    value = stack[-1] + stack[-2]
                    stack.append(value)
                    total += value
        return total