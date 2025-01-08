class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned_s = ''.join(c.lower() if c.isalnum() else '' for c in s)
        return cleaned_s == cleaned_s[::-1]
