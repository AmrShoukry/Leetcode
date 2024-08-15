class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        candies = [1] * length
        count = 0
        stack = []

        for index, rating in enumerate(ratings):
            if (index + 1 < length and ratings[index + 1] < ratings[index]):
                stack.append(index)
            else:
                if (index - 1 >= 0 and ratings[index - 1] < ratings[index]):
                    candies[index] = candies[index - 1] + 1
                count += candies[index]

                start_index = 2
                if(stack):
                    current_index = stack[0]
                    stack_length = len(stack)

                    for i in range(stack_length):
                        count += start_index
                        start_index += 1
                    
                    start_index -= 1
                    if (candies[current_index - 1] >= start_index and ratings[current_index - 1] < ratings[current_index]):
                        count += candies[current_index - 1] - start_index + 1
                    stack = []
        return count