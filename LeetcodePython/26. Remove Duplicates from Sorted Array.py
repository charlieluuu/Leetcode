class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        new = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[new] = nums[i]
                new += 1
        return new

if __name__ == '__main__':
    solution = Solution()
    result = solution.removeDuplicates([1, 1, 2])
    print(result)