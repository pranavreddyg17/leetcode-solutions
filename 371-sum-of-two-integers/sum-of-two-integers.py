class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF      # Mask to get last 32 bits
        MAX_INT = 0x7FFFFFFF   # Max positive 32-bit int

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK

        # If a is greater than MAX_INT, it means it's a negative number
        return a if a <= MAX_INT else ~(a ^ MASK)

