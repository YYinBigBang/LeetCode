class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        result = []

        for i in digits[::-1]:
            i += carry
            carry = i // 10
            result.insert(0, i % 10)

        if carry:
            result.insert(0, carry)

        return result

