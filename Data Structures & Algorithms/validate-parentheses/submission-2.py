class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        p = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        for c in s:
            if c not in p:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                pa = stack.pop()
                if p[c] != pa:
                    return False
        if len(stack) != 0:
            return False
        return True