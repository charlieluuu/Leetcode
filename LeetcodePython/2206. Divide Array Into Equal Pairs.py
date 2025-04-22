from collections import Counter

class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        count = Counter(nums)
        for i in count.values():
            if i % 2 != 0:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    result = solution.divideArray([3,2,3,2,2,2])
    print(result)