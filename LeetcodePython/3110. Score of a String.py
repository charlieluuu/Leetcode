class Solution:
    def scoreOfString(self, s: str) -> int:

        sum = 0

        for i in range(1, len(s)):
            a = ((ord(s[i])-ord(s[i-1])))
            ab = abs(a)
            sum += ab

        return sum

if __name__ == '__main__':
    solution = Solution()
    result = solution.scoreOfString("hello")
    print(result)