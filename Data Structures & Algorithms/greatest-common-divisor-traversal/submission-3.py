from collections import defaultdict
from math import gcd

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        graph = defaultdict(list)

        if 1 in nums:
            return False

        if len(set(nums)) == 1:
            return True

        for i in range(n):
            for j in range(n):
                if i != j and gcd(nums[i], nums[j]) > 1:
                    graph[nums[i]].append(nums[j])
                    graph[nums[j]].append(nums[i])

        visited = set()

        def dfs(node):
            visited.add(node)
            if node not in graph:
                return
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        dfs(nums[0])        
        return len(visited) == len(nums)