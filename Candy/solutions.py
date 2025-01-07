class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        size = len(ratings)
        candies = [1] * size  # fulfill the first condition

        # Left to right
        for i in range(1, size):
            if ratings[i-1] < ratings[i]:
                candies[i] = candies[i-1] + 1

        # Right to left
        for j in range(size-1, 0, -1):
            if ratings[j-1] > ratings[j]:
                # Use max() to prevent overriding the larger value already set
                candies[j-1] = max(candies[j-1], candies[j]+1)

        return sum(candies)
