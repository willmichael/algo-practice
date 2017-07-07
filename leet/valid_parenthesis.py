class Solution(object):
    def isValid(self, s):
        arr_s = list(s)
        ver = []
        compare = 0
        if len(arr_s) % 2 == 0:
            for c in arr_s:
                if c == ')':
                    if len(ver) == 0 or ver.pop() != '(':
                        return False
                elif c == ']':
                    if len(ver) == 0 or ver.pop() != '[':
                        return False
                elif c == '}': 
                    if len(ver) == 0 or ver.pop() != '{':
                        return False
                else:
                    ver.append(c)
            if len(ver) == 0:
                return True
        return False

s = "(()("
sol = Solution()
print sol.isValid(s)
