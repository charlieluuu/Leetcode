from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(sqrt(c)) + 1):
            b = sqrt (c - (a * a))
            if b % 1 == 0:
                return True
        return False

if __name__ == '__main__':
    solution = Solution()
    result = solution.judgeSquareSum(5)
    print(result)