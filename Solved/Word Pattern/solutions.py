class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        s = s.split(' ')
        if len(pattern) != len(s):
            return False

        seen = {}
        for i in range(len(pattern)):
            char = pattern[i]
            if char in seen.keys():
                if seen.get(char) != s[i]:
                    return False

            elif s[i] in seen.values():
                return False

            else:
                seen[char] = s[i]

        return True

