class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        low = 2
        high = x
        while low <= high:
            mid = low + (high - low) // 2

            if mid * mid > x:
                high = mid - 1
            elif mid * mid < x:
                low = mid + 1
            else:
                return mid

        return high

