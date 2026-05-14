class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.res = []
        candidates.sort()

        def track(i, cur, total):

            if total == target:
                self.res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            track(i+1, cur, total + candidates[i])
            cur.pop()
            while i < len(candidates)-1 and candidates[i+1] == candidates[i]:
                i += 1
            track(i+1, cur, total)

        track(0, [], 0)
        return self.res