class Solution(object):
    def simplifyPath(self, path):
        stack = []
        temp = ''
        path += '/'
        for p in path:
            if p == '/':
                if temp == '.':
                    temp = ''
                elif temp == '..':
                    if len(stack) >= 1:
                        stack.pop()
                    temp = ''
                else:
                    if temp != '':
                        stack.append(temp)
                        temp = ''
            else:
                temp += p
        res = '/'.join(stack)
        return '/' + res


s = Solution()
t = '/.'
s.simplifyPath(t)


