class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = {}

        for source, target, time in times:
            if source not in graph:
                graph[source] = []

            graph[source].append((target, time))
        
        distances = {}
        distances[k] = 0

        def dfs(source):

            if source not in graph:
                return
            
            for target, time in graph[source]:
                new_distance = distances[source] + time
                if target not in distances or new_distance < distances[target]:
                    distances[target] = new_distance
                    dfs(target)
        
        dfs(k)

        if len(distances) < n:
            return -1

        return max(distances.values())

                

