class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        arr = []
        res = []

        def isPalindrome(p):
            # boom!
            return p == p[::-1]

        def backtrack(a, total_length):

            if total_length == len(s):
                res.append(arr.copy())
                return

            pal = ""
            for i in range(len(a)):
                pal += a[i]
                if isPalindrome(pal):
                    arr.append(pal)
                    print("arr", a[i+1:])
                    backtrack(a[i+1:], total_length + i + 1)
                    arr.pop()
        
        backtrack(s, 0)
        return res