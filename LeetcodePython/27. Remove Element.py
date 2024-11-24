class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in nums:
            if i != val:
                nums[k] = i
                k += 1
        return k

if __name__ == '__main__':
    solution = Solution()
    result = solution.removeElement([3,2,2,3], 3)
    print(result)