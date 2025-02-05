class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []

        ranges = []
        start = end = nums[0]

        for n in nums[1:]:
            if n == end + 1:
                end = n
            else:
                ranges.append(f"{start}->{end}" if start != end else f"{start}")
                start = end = n
        ranges.append(f"{start}->{end}" if start != end else f"{start}")

        return ranges


if __name__ == '__main__':
    solution = Solution()
    result = solution.summaryRanges([0,1,2,4,5,7])
    print(result)