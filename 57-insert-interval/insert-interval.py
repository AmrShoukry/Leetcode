class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        length = len(intervals)
        cache_interval = newInterval
        solution = []
        general_modify = False
        overlapped = False
        for index, interval in enumerate(intervals):
            modified = False
            if not overlapped:
                if cache_interval[0] >= interval[0] and cache_interval[0] <= interval[1]:
                    cache_interval = [interval[0], max(interval[1], cache_interval[1])]
                    modified = True
                    general_modify = True
                elif cache_interval[0] <= interval[0] and cache_interval[1] >= interval[0]:
                    cache_interval = [cache_interval[0], max(interval[1], cache_interval[1])]
                    modified = True
                    general_modify = True
                if not modified:
                    if cache_interval[0] < interval[0] or general_modify == True:
                        solution.append(cache_interval)
                        overlapped = True
                    solution.append(interval)
            else:
                solution.append(interval)
        if overlapped == False:
            solution.append(cache_interval)
        return solution