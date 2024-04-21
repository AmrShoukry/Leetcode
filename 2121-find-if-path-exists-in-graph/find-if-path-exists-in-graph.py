class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjacent_hash = {}
        visited = [-1] * n

        for edge in edges:
            arr = adjacent_hash.get(edge[0])
            if arr is None:
                adjacent_hash[edge[0]] = [edge[1]]
            else:
                adjacent_hash[edge[0]].append(edge[1])
            arr = adjacent_hash.get(edge[1])
            if arr is None:
                adjacent_hash[edge[1]] = [edge[0]]
            else:
                adjacent_hash[edge[1]].append(edge[0])

        return self.check_validity(source, destination, visited, adjacent_hash)
        
    def check_validity(self, source, destination, visited, adjacent_hash):
        if visited[source] == 1:
            return False
        if source == destination:
            return True
        visited[source] = 1
        for adjacent in adjacent_hash[source]:
            if visited[adjacent] == -1:
                check = self.check_validity(adjacent, destination, visited, adjacent_hash)
                if check is True:
                    return True
        return False

