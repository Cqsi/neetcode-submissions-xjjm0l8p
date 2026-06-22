class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        # 1. Create hashmap of flight tickets
        flights = {}
        for source, target in tickets:
            if source not in flights:
                flights[source] = []
            flights[source].append(target)
        
        # 2. Heapify the adjacency lists in lexicographical order (it's automatic)
        for source in flights:
            heapq.heapify(flights[source])

        # 3. DFS, if we reach a source node without any targets, we append that source and start returning
        res = []
        def dfs(source):
            if source not in flights:
                res.append(source)
                return

            targets = flights[source]
            while targets:
                target = heapq.heappop(targets)
                dfs(target)
            
            res.append(source)
            return
        
        dfs("JFK")
        return res[::-1]
