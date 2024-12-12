class Solution1(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        # Convert the integer to a string and reverse it
        reversed_x = str(x)[::-1]

        return str(x) == reversed_x


class Solution2(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        original_x = x
        reversed_x = 0

        # Reverse the number
        while x > 0:
            reversed_x = reversed_x * 10 + x % 10
            x = x // 10

        return original_x == reversed_x
