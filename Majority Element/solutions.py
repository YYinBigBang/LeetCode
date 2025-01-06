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

