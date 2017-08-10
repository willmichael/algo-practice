class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == '' and p == '':
            return True
        elif p == '' and s!= '':
            return False
        elif s == '' and p != '':
            if len(p) > 1 and p[1] == '*':
                return self.isMatch(s, p[2:])
            else:
                return False
        elif s[0] == p[0] or p[0] == '.':
            if len(p) > 1 and p[1] == '*':
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:
                return self.isMatch(s[1:], p[1:])
        else:
            if len(p) > 1 and p[1] == '*':
                return self.isMatch(s, p[2:])
            else:
                return False

        



s = Solution()
pat = 'a*a*a*a*a*a*a*a*a*a*c'
query = 'aaaaaaaaaaaaab'
print s.isMatch(query, pat)
