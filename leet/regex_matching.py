class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_idx = 0
        p_idx = 0
        prev_char = ''
        repeat = 0

        for c in s:
            while True:
                if p_idx > len(p)-1:
                    return False
                elif c == p[p_idx]:
                    prev_char = p[p_idx]
                    p_idx += 1
                elif p_idx+1 < len(p)-1 and p[p_idx+1] == '*' and p[p_idx] != '.':
                    p_idx += 2
                    continue
                else:
                    if p[p_idx] == '.':
                        prev_char = p[p_idx]
                        p_idx += 1
                    elif p[p_idx] == '*':
                        if c == prev_char or prev_char == '.':
                            pass
                        elif p_idx+1 <= len(p)-1 and p[p_idx+1] == c:
                            p_idx += 2
                        else:
                            return False
                    else:
                        return False
                s_idx += 1
                break
        if p_idx != len(p):
            return False
        if s_idx != len(s):
            return False
        return True
                    
s = Solution()
pat = 'a*'
query = 'aa'
print s.isMatch(query, pat)
