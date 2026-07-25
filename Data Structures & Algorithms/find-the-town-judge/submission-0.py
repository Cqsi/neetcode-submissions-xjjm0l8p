class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        people = {}
        unique = set()

        for a, b in trust:
            unique.add(a)
            unique.add(b)

            if b not in people:
                people[b] = []
            people[b].append(a)
        
        judge = 0

        for p in people:
            if len(people[p]) == len(unique)-1:
                judge = p
        

        if judge == 0:
            return -1
        
        for value in people.values():
            if judge in value:
                return -1
        
        return judge