class Solution1(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = []
        for i in range(n):
            if i <= 2:
                steps.append(i + 1)
            else:
                steps.append(steps[i - 1] + steps[i - 2])

        return steps[n - 1]


class Solution2(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}

        def recursion(steps):
            if steps <= 2:
                return steps

            if steps not in memo:
                memo[steps] = recursion(steps - 1) + recursion(steps - 2)

            return memo[steps]

        return recursion(n)

