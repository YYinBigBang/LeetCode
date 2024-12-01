class Solution1(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary_recursion(left, right):
            if left > right:
                return -1
            # prevents overflow in midpoint calculation
            mid = left + (right - left) // 2

            if nums[mid] > target:
                return binary_recursion(left, mid - 1)
            elif nums[mid] < target:
                return binary_recursion(mid + 1, right)
            else:
                return mid

        return binary_recursion(0, len(nums) - 1)


class Solution2(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            # prevents overflow in midpoint calculation
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

