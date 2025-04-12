class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, c in enumerate(s):
            reversed_pos = 26 - (ord(c) - ord('a'))
            total += reversed_pos * (i + 1)
        return total

if __name__ == '__main__':
    solution = Solution()
    result = solution.reverseDegree("abc")
    print(result)