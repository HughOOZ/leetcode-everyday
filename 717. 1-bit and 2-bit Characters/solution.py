class MySolution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        result = []
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                i += 2
                result.append(2)
            elif bits[i] == 0:
                i += 1
                result.append(1)
        if result[-1] == 1:
            return True
        else:
            return False

'''Approach #1: Increment Pointer [Accepted]
Intuition and Algorithm

When reading from the i-th position, if bits[i] == 0, the next character must have 1 bit; else if bits[i] == 1, the next character must have 2 bits. We increment our read-pointer i to the start of the next character appropriately. At the end, if our pointer is at bits.length - 1, then the last character must have a size of 1 bit.'''
class Solution(object):
    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1

'''Approach #2: Greedy [Accepted]
Intuition and Algorithm

The second-last 0 must be the end of a character (or, the beginning of the array if it doesn't exist). Looking from that position forward, the array bits takes the form [1, 1, ..., 1, 0] where there are zero or more 1's present in total. It is easy to show that the answer is true if and only if there are an even number of ones present.

In our algorithm, we will find the second last zero by performing a linear scan from the right. We present two slightly different approaches below.'''
class Solution(object):
    def isOneBitCharacter(self, bits):
        parity = bits.pop()
        while bits and bits.pop(): parity ^= 1
        return parity == 0