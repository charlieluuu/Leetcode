class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.strip(" ")
        y = x.split()
        z= len(y[-1])
        return z

if __name__ == '__main__':
    solution = Solution()
    result = solution.lengthOfLastWord("Hello World")
    print(result)