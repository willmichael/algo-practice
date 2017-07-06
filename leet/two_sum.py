class Solution(object):
    def twoSum(self, nums, target):
        dict_diff = {}
        for i in range(len(nums)):
            if nums[i] in dict_diff:
                print [dict_diff[nums[i]], i]
                return [dict_diff[nums[i]], i]
            else:
                dict_diff[target - nums[i]] = i

        
def input():
    nums = [-1, -2, -3, -4, -5]
    target = -8

    return (nums, target)

def main():
    (nums, target) = input()

    sol = Solution()
    sol.twoSum(nums, target)


if __name__ == "__main__":
    main()
