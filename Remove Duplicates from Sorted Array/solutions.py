class Solution1(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[count] = nums[i]
                count += 1

        return count


class Solution2(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # set() removes duplicates
        # sorted() sorts the list
        # nums[:] = copies the sorted list back to nums
        nums[:] = sorted(set(nums))
        return len(nums)

