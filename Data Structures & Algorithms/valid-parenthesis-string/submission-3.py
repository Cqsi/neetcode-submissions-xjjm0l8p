class Solution:
    def checkValidString(self, s: str) -> bool:
        
        par = []
        star = []

        for i in range(len(s)):
            if s[i] == '(':
                par.append(i)
            elif s[i] == '*':
                star.append(i)
            else:
                if par:
                    par.pop()
                elif star:
                    star.pop()
                else:
                    return False        

        i = 0
        j = 0

        if par and not star:
            return False

        while i < len(par):

            if j == len(star):
                return False
            
            if par[i] < star[j]:
                i+=1
            
            j+=1

        return True