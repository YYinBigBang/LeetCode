class Solution1(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        avg = len(nums) // 2
        count = 0
        element = nums[0]
        for num in nums:

            if num == element:
                count += 1
            else:
                count = 1
                element = num

            if count > avg:
                return element


class Solution1(object):
    def majorityElement(self, nums):
        """
        Boyer-Moore Voting Algorithm:
        Finds the majority element by maintaining a single candidate and a vote counter.
        It incrementally adjusts the vote based on whether the current element matches the candidate,
        ensuring that the majority element dominates by the end.
        """

        count = 0
        candidate = None

        for num in nums:
            # If count is 0, then the current element is the candidate
            if count == 0:
                candidate = num
                count += 1

            # If the current element is the same as the candidate, increment the count
            elif num == candidate:
                count += 1

            # If the current element is different from the candidate, decrement the count
            else:
                count -= 1

        return candidate
