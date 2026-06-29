class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        res = 0
        carry = 0

        for i in range(32):
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1

            # sum bit: XOR of both bits and carry
            curr_bit = bit_a ^ bit_b ^ carry

            # put curr_bit into result at position i
            res |= curr_bit << i

            # carry happens if at least two of bit_a, bit_b, carry are 1
            carry = (bit_a & bit_b) | (bit_a & carry) | (bit_b & carry)

        # If res is bigger than max signed 32-bit int,
        # interpret it as a negative two's complement number.
        if res > MAX_INT:
            res = ~(res ^ MASK)

        return res