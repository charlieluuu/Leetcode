class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
        return len(nums)


if __name__ == '__main__':
    solution = Solution()
    result = solution.searchInsert([1,3,5,6], 5)
    print(result)