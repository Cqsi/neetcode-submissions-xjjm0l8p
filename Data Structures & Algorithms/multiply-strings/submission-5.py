class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                digit1 = ord(num1[i]) - ord("0")
                digit2 = ord(num2[j]) - ord("0")

                product = digit1 * digit2

                right = i + j + 1
                left = i + j

                total = product + res[right]

                res[right] = total % 10
                res[left] += total // 10

        # remove leading zeroes
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1

        return "".join(str(digit) for digit in res[start:])