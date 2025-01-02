class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        list1 = []
        list2 = []

        for i in set1:
            if i not in set2:
                list1.append(i)

        for j in set2:
            if j not in set1:
                list2.append(j)

        return [list1, list2]

    