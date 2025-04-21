class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        total = 0
        n = len(arr)

        for i in range(n):
            for end in range(i, n):
                if (end - i + 1) % 2 == 1:
                    total += sum(arr[i:end + 1])

        return total


if __name__ == '__main__':
    solution = Solution()
    result = solution.sumOddLengthSubarrays([1,4,2,5,3])
    print(result)