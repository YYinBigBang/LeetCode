class Solution1(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        sum_str = ""

        while a or b:
            num1 = num2 = 0

            if a:
                num1 = int(a[-1])
                a = a[:-1]
            if b:
                num2 = int(b[-1])
                b = b[:-1]

            total = num1 + num2 + carry
            carry = total // 2

            sum_str = str(total % 2) + sum_str

        if carry:
            return str(carry) + sum_str
        return sum_str


class Solution2(object):
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]


class Solution3(object):
    def addBinary(self, a, b):
        return format(int(a, 2) + int(b, 2), "b")

