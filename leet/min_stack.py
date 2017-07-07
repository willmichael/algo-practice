class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.min == None:
            print "not"
            self.stack.append((x, x))
            self.min = x
        else:
            if x < self.min:
                print "new"
                print self.min
                print x
                self.stack.append((x,x))
                self.min = x
            else:
                print "else"
                print self.min
                print (x, self.min)
                self.stack.append((x,self.min))

    def pop(self):
        """
        :rtype: void
        """
        print self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack) - 1 ][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack) - 1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
