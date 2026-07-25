from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        dead = set(deadends)

        if "0000" in dead:
            return -1

        queue = deque([("0000", 0)])
        visited = set()
        visited.add("0000")

        while queue:
            current, turns = queue.popleft()

            if current == target:
                return turns
            
            for i in range(4):
                digit = int(current[i])

                forward_digit = (digit + 1) % 10
                forward_code = current[:i] + str(forward_digit) + current[i + 1:]

                if forward_code not in dead and forward_code not in visited:
                    visited.add(forward_code)
                    queue.append((forward_code, turns + 1))
                
                backward_digit = (digit - 1) % 10
                backward_code = current[:i] + str(backward_digit) + current[i + 1:]

                if backward_code not in dead and backward_code not in visited:
                    visited.add(backward_code)
                    queue.append((backward_code, turns + 1))
        
        return -1
