class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        dig = len(digits)
        val = digits[dig - 1]

        if dig == 1 and val == 9:
            return [1,0]

        while digits[dig-1] == 9:
            digits[dig-1] = 0
            if dig-1 == 0:
                digits = [1] + digits
                return digits
            dig -= 1

        digits[dig-1] += 1
        return digits

s = Solution()
print s.plusOne([9,9])
