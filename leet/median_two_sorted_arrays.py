import os
import math


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        size1 = len(nums1)
        size2 = len(nums2)
        size = size1 + size2

        res_size = 0
        idx1 = 0
        idx2 = 0
        res = []
        is_even = 0

        if size % 2 == 0:
            is_even = 1

        if size1 == 0:
            res = nums2
        elif size2 == 0:
            res = nums1
        else:
            while res_size != size:
                if nums1[idx1] > nums2[idx2]:
                    res.append(nums2[idx2])
                    idx2 += 1
                else:
                    res.append(nums1[idx1])
                    idx1 += 1
                if idx1 >= size1:
                    for i in range(idx2, size2):
                        res.append(nums2[i])
                    break
                if idx2 >= size2:
                    for i in range(idx1, size1):
                        res.append(nums1[i])
                    break
                res_size += 1

        idx = int(math.ceil(size/float(2))) - 1

        if is_even == 0:
            return res[idx]
        else:
            return ((res[idx] + res[idx + 1]) / float(2))

def input():
    nums1 = [1, 2]
    nums2 = [3, 4]

    return (nums1, nums2)

def main():
    (nums1, nums2) = input()

    sol = Solution()
    sol.findMedianSortedArrays(nums1, nums2)


if __name__ == "__main__":
    main()
