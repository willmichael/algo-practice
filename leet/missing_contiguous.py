# Given a contiguous sequence of numbers in which each number repeats thrice, there is exactly one missing number. Find the missing number.
# eg: 11122333 : Missing number 2
# 11122233344455666 Missing number 5



def find_missing(seq):
    for i in range(2, len(seq), 3):
        num = (i+1)/3
        if int(seq[i]) == num:
            pass
        else:
            print 'missing', num
            return num


seq = "11122333"
find_missing(seq)

