from collections import defaultdict
class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        total_distinct = len(set(nums))
        n = len(nums)
        result = 0

        for i in range(n):
            freq = defaultdict(int)
            distinct_count = 0
            for j in range(i, n):
                if freq[nums[j]] == 0:
                    distinct_count += 1
                freq[nums[j]] += 1

                if distinct_count == total_distinct:
                    result += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    result = solution.countCompleteSubarrays([1,3,1,2,2])
    print(result)