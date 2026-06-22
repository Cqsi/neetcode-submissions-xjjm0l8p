class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        flights = {}

        for source, target in tickets:
            if source not in flights:
                flights[source] = []
            flights[source].append(target)
        
        for source in flights:
            heapq.heapify(flights[source])

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
