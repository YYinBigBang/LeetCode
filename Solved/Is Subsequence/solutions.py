class Solution1(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for char in t:
            if not s:
                return True

            if char == s[0]:
                s = s[1:]

        return False if s else True


class Solution2(object):
    def isSubsequence(self, s, t):
        index = 0
        for c in t:
            if index < len(s) and s[index] == c:
                index += 1

        return index == len(s)

