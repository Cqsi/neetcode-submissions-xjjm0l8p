from operator import itemgetter

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        res = 0
        stack = []
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(key=itemgetter(0))

        for p2, s2 in cars:
            if not stack:
                stack.append((p2, s2))
            else:
                # we have to make a loop
                # our goal is to add the car fleet
                p1, s1 = stack[-1]
                if s2 >= s1:
                    stack.append((p2, s2))
                else:
                    while stack and not s2>=s1:
                        t = (p2-p1)/(s1-s2) # time when the cars meet
                        pmeet = p1+s1*t # position where they meet
                        if pmeet <= target:
                            stack.pop()
                            if stack:
                                p1, s1 = stack[-1]
                        else:
                            break
                    stack.append(((p2, s2))) # add the car fleet to the stack

        return len(stack)
        # HOLE SHIT WE GOT IT
        
