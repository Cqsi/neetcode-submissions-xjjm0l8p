class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            ct = temperatures[i]
            if not stack:
                stack.append((i, ct))
            elif ct <= stack[-1][1]:
                stack.append((i, ct))
            else:
                while stack and stack[-1][1] < ct:
                    j, t = stack.pop()
                    res[j] = i-j
                stack.append((i, ct))
            print(stack)

        return res