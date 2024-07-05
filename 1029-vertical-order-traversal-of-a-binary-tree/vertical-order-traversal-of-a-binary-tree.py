# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        positions = {}
        solution = []
        nodes = [[root, 0, 0]]
        while nodes:
            [node, row, column] = nodes.pop(0)
            if node.left:
                nodes.append([node.left, row + 1, column - 1])
            if node.right:
                nodes.append([node.right, row + 1, column + 1])
            position = positions.get(column, -1)
            if position == -1:
                positions[column] = {
                    row: [node.val]
                } 
            else:
                rowPosition = positions[column].get(row, -1)
                print(rowPosition)
                if rowPosition == -1:
                    positions[column][row] = [node.val]
                else:
                    positions[column][row].append(node.val)
                    positions[column][row] = sorted(positions[column][row])


        heap = []

        for column, elements in positions.items():
            finalColumn = []
            for row, values in elements.items():
                for value in values:
                    finalColumn.append(value)
            heap.append([column, finalColumn])
        heapq.heapify(heap)

        while heap:
            solution.append(heapq.heappop(heap)[1])
    
        return solution

