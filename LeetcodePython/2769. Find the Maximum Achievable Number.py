class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + t + t

if __name__ == '__main__':
    solution = Solution()
    result = solution.theMaximumAchievableX(4, 1)
    print(result)