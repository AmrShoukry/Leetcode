import math

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        length = len(matrix)
        number_of_pointers = length
        pointers = {}
        counter = 0

        for i in range(number_of_pointers):
            pointers[i] = -1

        while counter < k:
            for i in range(number_of_pointers):
                if pointers[i] + 1 < length:
                    minimum_element = matrix[i][pointers[i] + 1]
                    minimum_pointer = i
                    break
            for key, value in pointers.items():
                if value + 1 < length and matrix[key][value + 1] < minimum_element:
                    minimum_element = matrix[key][value + 1]
                    minimum_pointer = key
            pointers[minimum_pointer] += 1
            counter += 1

        return matrix[minimum_pointer][pointers[minimum_pointer]]
            
        