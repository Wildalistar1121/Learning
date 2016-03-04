class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4 != 0


Number = int(raw_input('Enter Number: '))
print Solution().canWinNim(Number)