class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        self.res = []

        def par(cur, op, cl):

            if len(cur) == 2*n:
                self.res.append(cur)
                return
            
            if op < n:
                par(cur + "(", op+1, cl)
            if cl < op:
                par(cur + ")", op, cl+1)
        
        par("", 0, 0)
        return self.res


            