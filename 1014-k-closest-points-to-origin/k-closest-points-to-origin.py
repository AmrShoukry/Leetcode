class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = sorted(points, key=lambda point: math.sqrt(math.pow(point[0], 2) + math.pow(point[1], 2)))
        return distances[:k]