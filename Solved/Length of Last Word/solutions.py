class Solution1(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        for char in s[::-1]:
            if char == " " and length == 0:
                continue
            elif char == " " and length > 0:
                break
            else:
                length += 1

        return length


class Solution2(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Split the string by whitespace and remove leading and trailing whitespaces
        list_s = s.strip().split()
        return len(list_s[-1])

