class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0

        for i in range(32):
            # Gets us the last bit of n
            bit = n & 1

            # Make space in res
            res <<= 1

            # Add the bit
            res |= bit

            # Remove the last bit from n
            n >>= 1

        return res
