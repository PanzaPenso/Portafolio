import math
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        number = str(x)
        total_len = len(number)
        half_len = math.floor(total_len / 2)
        i = 0
        j = total_len - 1
        palindrome = True
        while i < half_len:
            if number[i] != number[j]:
                palindrome = False
                break
            else:
                i += 1
                j -= 1
        return palindrome