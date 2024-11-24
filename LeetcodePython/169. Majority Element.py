class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums = sorted(nums)
        middle = (len(nums)) // 2

        return nums[middle]

if __name__ == '__main__':
    solution = Solution()
    result = solution.majorityElement([3, 2, 3])
    print(result)