class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        res = []
        d = str(digits)

        def loop(cur, i):
            if i == len(digits):
                res.append(cur)
                return
            
            dig = int(d[i])
            for c in m[dig]:
                loop(cur+c, i+1)

        if len(digits) == 0:
            return []
        else: 
            loop("", 0)
            return res
