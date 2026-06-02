class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []

        for o in operations:

            if o == '+':
                a = stack[-2]
                b = stack[-1]
                stack.append(a+b)
            elif o == 'D':
                d = stack[-1]
                stack.append(2*d)
            elif o == 'C':
                stack.pop()
            else:
                stack.append(int(o))
            
            print(stack)
                
        return sum([int(x) for x in stack])